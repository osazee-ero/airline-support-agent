import base64
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.airline_tools import (
    check_flight_status,
    get_booking_details,
    check_baggage_allowance,
    create_refund_request,
    change_seat,
    escalate_to_human_agent,
)


load_dotenv()

MODEL = "gpt-5.5"


TOOL_FUNCTIONS = {
    "check_flight_status": check_flight_status,
    "get_booking_details": get_booking_details,
    "check_baggage_allowance": check_baggage_allowance,
    "create_refund_request": create_refund_request,
    "change_seat": change_seat,
    "escalate_to_human_agent": escalate_to_human_agent,
}


TOOLS = [
    {
        "type": "function",
        "name": "check_flight_status",
        "description": "Check the status, gate, terminal, and timing of a flight.",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_number": {
                    "type": "string",
                    "description": "The flight number, for example BA249 or AC857."
                }
            },
            "required": ["flight_number"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "get_booking_details",
        "description": "Look up passenger booking details using a booking reference.",
        "parameters": {
            "type": "object",
            "properties": {
                "booking_reference": {
                    "type": "string",
                    "description": "The booking reference, for example AB1234."
                }
            },
            "required": ["booking_reference"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "check_baggage_allowance",
        "description": "Check baggage allowance for a ticket class.",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_class": {
                    "type": "string",
                    "description": "The ticket class, such as Economy, Premium Economy, or Business."
                }
            },
            "required": ["ticket_class"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "create_refund_request",
        "description": "Create a simulated refund request for a booking.",
        "parameters": {
            "type": "object",
            "properties": {
                "booking_reference": {
                    "type": "string",
                    "description": "The booking reference, for example AB1234."
                }
            },
            "required": ["booking_reference"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "change_seat",
        "description": "Change a passenger seat for a booking.",
        "parameters": {
            "type": "object",
            "properties": {
                "booking_reference": {
                    "type": "string",
                    "description": "The booking reference, for example AB1234."
                },
                "new_seat": {
                    "type": "string",
                    "description": "The new seat number, for example 15C."
                }
            },
            "required": ["booking_reference", "new_seat"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "escalate_to_human_agent",
        "description": "Escalate a difficult support request to a human support agent.",
        "parameters": {
            "type": "object",
            "properties": {
                "reason": {
                    "type": "string",
                    "description": "The reason the request should be escalated."
                }
            },
            "required": ["reason"],
            "additionalProperties": False
        },
        "strict": True
    },
]


SYSTEM_INSTRUCTIONS = """
You are a helpful airline customer support agent.

You help passengers with:
- Flight status
- Booking details
- Baggage allowance
- Refund requests
- Seat changes
- Escalation to a human support agent

Use the available tools when the user asks for information that requires airline data.

Be polite, clear, and concise.

Important:
- This is a demo app using fake airline data.
- Do not claim to access real airline systems.
- If information is missing, ask the user for the missing flight number, booking reference, ticket class, or seat.
"""


def get_openai_client() -> OpenAI:
    """
    Create the OpenAI client using the API key from the .env file.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY was not found. Please check your .env file.")

    return OpenAI(api_key=api_key)


def build_user_context(
    user_message: str,
    passenger_name: str = "",
    booking_reference: str = "",
    flight_number: str = "",
    chat_history: list[dict] | None = None,
) -> str:
    """
    Combine the user's message, passenger details, and recent chat history.
    """

    history_text = ""

    if chat_history:
        recent_messages = chat_history[-6:]

        for message in recent_messages:
            role = message.get("role", "unknown")
            content = message.get("content", "")
            history_text += f"{role}: {content}\n"

    return f"""
Passenger name: {passenger_name or "Not provided"}
Booking reference: {booking_reference or "Not provided"}
Flight number: {flight_number or "Not provided"}

Recent conversation:
{history_text or "No previous conversation."}

Latest user message:
{user_message}
"""


def run_tool(tool_name: str, arguments: dict) -> dict:
    """
    Run the correct Python function using the tool name chosen by the AI.
    """

    tool_function = TOOL_FUNCTIONS.get(tool_name)

    if not tool_function:
        return {
            "success": False,
            "message": f"Unknown tool: {tool_name}"
        }

    return tool_function(**arguments)


def ask_airline_agent(
    user_message: str,
    passenger_name: str = "",
    booking_reference: str = "",
    flight_number: str = "",
    chat_history: list[dict] | None = None,
) -> dict:
    """
    Send the user message to the AI agent.

    The agent can either:
    1. Answer directly
    2. Call one of our airline tools, then explain the result
    """

    client = get_openai_client()

    user_context = build_user_context(
    user_message=user_message,
    passenger_name=passenger_name,
    booking_reference=booking_reference,
    flight_number=flight_number,
    chat_history=chat_history,
        )

    first_response = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_INSTRUCTIONS,
        input=user_context,
        tools=TOOLS,
    )

    function_call = None

    for item in first_response.output:
        if item.type == "function_call":
            function_call = item
            break

    if function_call is None:
        return {
            "answer": first_response.output_text,
            "tool_called": None,
            "tool_arguments": None,
            "tool_result": None,
        }

    tool_name = function_call.name
    tool_arguments = json.loads(function_call.arguments)

    tool_result = run_tool(tool_name, tool_arguments)

    second_response = client.responses.create(
    model=MODEL,
    instructions=SYSTEM_INSTRUCTIONS,
    previous_response_id=first_response.id,
    input=[
        {
            "type": "function_call_output",
            "call_id": function_call.call_id,
            "output": json.dumps(tool_result),
        }
    ],
    tools=TOOLS,
)

    return {
        "answer": second_response.output_text,
        "tool_called": tool_name,
        "tool_arguments": tool_arguments,
        "tool_result": tool_result,
    }

def analyze_travel_document(
    image_bytes: bytes,
    mime_type: str,
    user_message: str = "",
) -> str:
    """
    Analyze an uploaded travel document image.

    This can be used for boarding passes, baggage tags, travel screenshots,
    or airline receipts.
    """

    client = get_openai_client()

    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = f"""
You are an airline customer support assistant.

Analyze the uploaded travel document image.

The user said:
{user_message or "No specific question provided."}

Extract any visible travel-related information, such as:
- Passenger name
- Airline
- Flight number
- Booking reference
- Departure city
- Arrival city
- Date or time
- Gate
- Seat
- Boarding time
- Baggage details

Important:
- Only mention information that is visible or reasonably clear.
- If something is unclear, say that it is unclear.
- Do not invent missing details.
- This is a demo app, not a real airline system.
"""

    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": prompt,
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{mime_type};base64,{encoded_image}",
                    },
                ],
            }
        ],
    )

    return response.output_text


if __name__ == "__main__":
    response = ask_airline_agent(
        user_message="Is my flight BA249 delayed?",
        flight_number="BA249",
    )

    print("Answer:")
    print(response["answer"])

    print("\nTool called:")
    print(response["tool_called"])

    print("\nTool arguments:")
    print(response["tool_arguments"])

    print("\nTool result:")
    print(response["tool_result"])