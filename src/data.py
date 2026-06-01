FAKE_FLIGHTS = {
    "BA249": {
        "airline": "British Airways",
        "flight_number": "BA249",
        "origin": "London Heathrow",
        "destination": "Toronto Pearson",
        "departure_time": "08:30 AM",
        "arrival_time": "11:45 AM",
        "gate": "B12",
        "terminal": "Terminal 5",
        "status": "On Time",
    },
    "AC857": {
        "airline": "Air Canada",
        "flight_number": "AC857",
        "origin": "London Heathrow",
        "destination": "Toronto Pearson",
        "departure_time": "03:00 PM",
        "arrival_time": "06:10 PM",
        "gate": "C8",
        "terminal": "Terminal 2",
        "status": "Delayed by 45 minutes",
    },
    "DL401": {
        "airline": "Delta Airlines",
        "flight_number": "DL401",
        "origin": "New York JFK",
        "destination": "Atlanta",
        "departure_time": "12:15 PM",
        "arrival_time": "02:40 PM",
        "gate": "A4",
        "terminal": "Terminal 4",
        "status": "Boarding",
    },
}


FAKE_BOOKINGS = {
    "AB1234": {
        "booking_reference": "AB1234",
        "passenger_name": "Jane Doe",
        "flight_number": "BA249",
        "seat": "14A",
        "ticket_class": "Economy",
        "checked_bags": 1,
        "booking_status": "Confirmed",
    },
    "CD5678": {
        "booking_reference": "CD5678",
        "passenger_name": "John Smith",
        "flight_number": "AC857",
        "seat": "3C",
        "ticket_class": "Business",
        "checked_bags": 2,
        "booking_status": "Confirmed",
    },
    "EF9012": {
        "booking_reference": "EF9012",
        "passenger_name": "Mary Johnson",
        "flight_number": "DL401",
        "seat": "22F",
        "ticket_class": "Economy",
        "checked_bags": 0,
        "booking_status": "Checked In",
    },
}


BAGGAGE_POLICIES = {
    "Economy": {
        "carry_on": "1 carry-on bag and 1 personal item",
        "checked_bag": "1 checked bag up to 23kg",
        "extra_bag_fee": "$75 per extra checked bag",
    },
    "Premium Economy": {
        "carry_on": "1 carry-on bag and 1 personal item",
        "checked_bag": "2 checked bags up to 23kg each",
        "extra_bag_fee": "$60 per extra checked bag",
    },
    "Business": {
        "carry_on": "2 carry-on bags and 1 personal item",
        "checked_bag": "2 checked bags up to 32kg each",
        "extra_bag_fee": "$50 per extra checked bag",
    },
}


REFUND_RULES = {
    "Economy": "Refunds may be available depending on ticket conditions. A cancellation fee may apply.",
    "Premium Economy": "Refunds are usually available with reduced cancellation fees.",
    "Business": "Refunds are usually flexible and may be processed with little or no fee.",
}