import streamlit as st


st.set_page_config(
    page_title="Airline AI Support Agent",
    page_icon="✈️",
    layout="wide"
)


st.title("✈️ Airline AI Support Agent")

st.write(
    """
    This app will become a multi-modal airline customer support assistant.
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


st.subheader("Chat with the Support Agent")

user_message = st.text_area(
    "Your message",
    placeholder="Example: Is my flight delayed? What is my baggage allowance?"
)


if st.button("Send Message"):
    if not user_message:
        st.warning("Please enter a message before sending.")
    else:
        st.info("The AI support agent logic will be added soon.")

        st.write("### Current Input")
        st.write(f"Passenger name: {passenger_name}")
        st.write(f"Booking reference: {booking_reference}")
        st.write(f"Flight number: {flight_number}")
        st.write(f"Message: {user_message}")

        if uploaded_file:
            st.write(f"Uploaded file: {uploaded_file.name}")
