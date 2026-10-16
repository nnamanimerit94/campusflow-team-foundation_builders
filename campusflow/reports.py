
#assign ticket to staff
def assign_ticket(tickets):
    """Assign a support ticket to a staff member."""

    if not tickets:
        print("No tickets available for assignment.")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    staff_name = input("Enter staff member's name: ").strip()

    if not staff_name:
        print("Staff name cannot be empty.")
        return

    tickets[ticket_id]["assigned_to"] = staff_name

    print(f"Ticket {ticket_id} has been assigned to {staff_name}.")
