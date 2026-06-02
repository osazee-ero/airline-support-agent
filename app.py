import streamlit as st
from src.agent import ask_airline_agent
from src.airline_tools import (
    check_flight_status,
    get_booking_details,
    check_baggage_allowance,
    create_refund_request,
    change_seat,
    escalate_to_human_agent,
)


st.set_page_config(
    page_title="Airline AI Support Agent",
    page_icon="✈️",
    layout="wide"
)


st.title("✈️ Airline AI Support Agent")

st.write(
    """
    This app is a multi-modal airline customer support assistant.
    It will help passengers with flight status, baggage allowance, bookings,
    refunds, seat changes, and uploaded travel documents.
    """
)


st.subheader("Passenger Details")

col1, col2, col3 = st.columns(3)

with col1:
    passenger_name = st.text_input("Passenger name", placeholder="Example: Jane Doe")

with col2:
    booking_reference = st.text_input("Booking reference", placeholder="Example: AB1234")

with col3:
    flight_number = st.text_input("Flight number", placeholder="Example: BA249")


st.subheader("Upload Travel Document")

uploaded_file = st.file_uploader(
    "Upload a boarding pass, baggage tag, or travel screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded travel document", width=350)


st.subheader("Quick Support Tools")

st.write(
    """
    These buttons directly call the backend airline support tools.
    Later, the AI agent will decide which of these tools to call automatically.
    """
)


tool_col1, tool_col2, tool_col3 = st.columns(3)

with tool_col1:
    if st.button("Check Flight Status"):
        if not flight_number:
            st.warning("Please enter a flight number first.")
        else:
            result = check_flight_status(flight_number)
            st.json(result)

with tool_col2:
    if st.button("Get Booking Details"):
        if not booking_reference:
            st.warning("Please enter a booking reference first.")
        else:
            result = get_booking_details(booking_reference)
            st.json(result)

with tool_col3:
    ticket_class = st.selectbox(
        "Ticket class",
        ["Economy", "Premium Economy", "Business"]
    )

    if st.button("Check Baggage Allowance"):
        result = check_baggage_allowance(ticket_class)
        st.json(result)


st.subheader("Booking Actions")

action_col1, action_col2, action_col3 = st.columns(3)

with action_col1:
    if st.button("Create Refund Request"):
        if not booking_reference:
            st.warning("Please enter a booking reference first.")
        else:
            result = create_refund_request(booking_reference)
            st.json(result)

with action_col2:
    new_seat = st.text_input("New seat", placeholder="Example: 15C")

    if st.button("Change Seat"):
        if not booking_reference or not new_seat:
            st.warning("Please enter both booking reference and new seat.")
        else:
            result = change_seat(booking_reference, new_seat)
            st.json(result)

with action_col3:
    escalation_reason = st.text_area(
        "Escalation reason",
        placeholder="Example: Passenger needs urgent refund help."
    )

    if st.button("Escalate to Human Agent"):
        if not escalation_reason:
            st.warning("Please enter a reason for escalation.")
        else:
            result = escalate_to_human_agent(escalation_reason)
            st.json(result)


st.subheader("Chat with the Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Ask about your flight, booking, baggage, refund, or seat...")

if user_message:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    try:
        with st.spinner("Agent is thinking..."):
            response = ask_airline_agent(
                user_message=user_message,
                passenger_name=passenger_name,
                booking_reference=booking_reference,
                flight_number=flight_number,
            )

        assistant_answer = response["answer"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": assistant_answer,
            }
        )

        with st.chat_message("assistant"):
            st.write(assistant_answer)

            if response["tool_called"]:
                with st.expander("Tool call details"):
                    st.write("Tool called:")
                    st.code(response["tool_called"])

                    st.write("Tool arguments:")
                    st.json(response["tool_arguments"])

                    st.write("Tool result:")
                    st.json(response["tool_result"])

    except Exception as error:
        error_message = f"Something went wrong: {error}"

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": error_message,
            }
        )

        with st.chat_message("assistant"):
            st.error(error_message)

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()