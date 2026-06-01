from src.data import FAKE_FLIGHTS, FAKE_BOOKINGS, BAGGAGE_POLICIES, REFUND_RULES


def check_flight_status(flight_number: str) -> dict:
    """
    Look up fake flight status using a flight number.
    """

    flight_number = flight_number.upper().strip()

    flight = FAKE_FLIGHTS.get(flight_number)

    if not flight:
        return {
            "success": False,
            "message": f"No flight found for flight number {flight_number}."
        }

    return {
        "success": True,
        "flight": flight
    }


def get_booking_details(booking_reference: str) -> dict:
    """
    Look up fake booking details using a booking reference.
    """

    booking_reference = booking_reference.upper().strip()

    booking = FAKE_BOOKINGS.get(booking_reference)

    if not booking:
        return {
            "success": False,
            "message": f"No booking found for reference {booking_reference}."
        }

    return {
        "success": True,
        "booking": booking
    }


def check_baggage_allowance(ticket_class: str) -> dict:
    """
    Look up baggage allowance using ticket class.
    """

    ticket_class = ticket_class.strip().title()

    policy = BAGGAGE_POLICIES.get(ticket_class)

    if not policy:
        return {
            "success": False,
            "message": f"No baggage policy found for ticket class {ticket_class}."
        }

    return {
        "success": True,
        "ticket_class": ticket_class,
        "baggage_policy": policy
    }


def create_refund_request(booking_reference: str) -> dict:
    """
    Simulate creating a refund request for a booking.
    """

    booking_reference = booking_reference.upper().strip()

    booking = FAKE_BOOKINGS.get(booking_reference)

    if not booking:
        return {
            "success": False,
            "message": f"No booking found for reference {booking_reference}."
        }

    ticket_class = booking["ticket_class"]
    refund_rule = REFUND_RULES.get(ticket_class, "Refund policy unavailable.")

    return {
        "success": True,
        "booking_reference": booking_reference,
        "passenger_name": booking["passenger_name"],
        "ticket_class": ticket_class,
        "refund_rule": refund_rule,
        "refund_status": "Refund request created for review."
    }


def change_seat(booking_reference: str, new_seat: str) -> dict:
    """
    Simulate changing a passenger's seat.
    """

    booking_reference = booking_reference.upper().strip()
    new_seat = new_seat.upper().strip()

    booking = FAKE_BOOKINGS.get(booking_reference)

    if not booking:
        return {
            "success": False,
            "message": f"No booking found for reference {booking_reference}."
        }

    old_seat = booking["seat"]
    booking["seat"] = new_seat

    return {
        "success": True,
        "booking_reference": booking_reference,
        "passenger_name": booking["passenger_name"],
        "old_seat": old_seat,
        "new_seat": new_seat,
        "message": f"Seat changed from {old_seat} to {new_seat}."
    }


def escalate_to_human_agent(reason: str) -> dict:
    """
    Simulate escalating the support request to a human agent.
    """

    return {
        "success": True,
        "status": "Escalated",
        "reason": reason,
        "message": "This request has been escalated to a human support agent."
    }