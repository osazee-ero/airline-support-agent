# Airline AI Support Agent

A multi-modal airline customer support agent that uses Large Language Models, function calling, and image understanding to help passengers with common airline support tasks.

## Project Overview

This project is part of my LLM Engineering portfolio. The goal is to build a practical AI customer support assistant for an airline.

The assistant will be able to answer passenger questions, call backend functions, retrieve fake airline data, and support image uploads such as boarding passes or travel documents.

## Problem

Airline passengers often need quick help with flight status, baggage allowance, booking details, seat changes, refunds, and travel documents.

Traditional support systems can be slow, repetitive, and difficult to navigate.

## Solution

This app provides an AI-powered support agent that can:

* Chat with users through a simple interface
* Understand airline-related support questions
* Call backend functions to retrieve structured information
* Use fake airline data to simulate real support workflows
* Accept uploaded images for multi-modal support
* Respond in a clear and helpful way

## Features

- Streamlit customer support interface
- Passenger details input
- Fake flight status lookup
- Fake booking lookup
- Baggage allowance checker
- Refund request simulator
- Seat change simulator
- Escalation to human support
- AI agent with function calling
- Tool call details display
- Chat-style conversation history
- Recent conversation context for follow-up questions
- Image upload for boarding passes or travel screenshots
- Multi-modal travel document analysis

## Tech Stack

* Python
* Streamlit
* OpenAI API
* Function calling
* Vision-capable LLM
* Fake airline data
* GitHub
* Streamlit Community Cloud

## Project Structure

```text
airline-support-agent/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── __init__.py
│   ├── airline_tools.py
│   ├── agent.py
│   ├── data.py
│   └── utils.py
├── notebooks/
├── screenshots/
└── examples/
```

## Application Workflow

```text
User asks a question or uploads an image
        ↓
App sends the message to the AI agent
        ↓
Agent decides whether a tool/function is needed
        ↓
Backend function retrieves fake airline data
        ↓
Agent creates a helpful customer support response
        ↓
User sees the answer in the chat interface
```

## Example Questions

```text
Is my flight BA249 delayed?
What is my baggage allowance?
Can I change my seat?
Can I request a refund?
Can you read this boarding pass?
What is the status of booking AB1234?
```

## How to Run

```bash
git clone https://github.com/ememosazee19991990/airline-support-agent.git
cd airline-support-agent
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Environment Variables

Create a `.env` file using the example below:

```env
OPENAI_API_KEY=your_api_key_here
```

Do not upload your real `.env` file to GitHub.

## Status

Core version completed.

Current version includes:

- Manual support tools
- AI agent support
- Function calling
- Chat history
- Conversation context
- Uploaded travel document analysis

## What I Learned

Through this project, I practiced:

- Building a customer-support style LLM application
- Creating fake structured data for testing AI workflows
- Writing backend tools that simulate airline support functions
- Connecting tools to a Streamlit UI
- Implementing LLM function calling
- Showing tool call details for transparency
- Managing chat history with Streamlit session state
- Passing recent conversation context to an AI agent
- Adding multi-modal image analysis for uploaded travel documents
- Keeping API keys safe with environment variables

## Demo

Live demo will be added after deployment.

## Screenshots

Screenshots will be added after the app is built.
