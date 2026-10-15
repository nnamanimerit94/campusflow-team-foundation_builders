def update_ticket_status(tickets):
    """Update the status of a support ticket."""

    if not tickets:
        print("No tickets available.")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    print(f"\nCurrent status: {tickets[ticket_id]['status']}")

    print("\nSelect the new status:")
    print("1. Open")
    print("2. In Progress")
    print("3. Resolved")
    print("4. Closed")

    choice = input("Enter your choice: ").strip()

    statuses = {
        "1": "open",
        "2": "in_progress",
        "3": "resolved",
        "4": "closed"
    }

    if choice not in statuses:
        print("Invalid choice. Status was not changed.")
        return

    tickets[ticket_id]["status"] = statuses[choice]

    print(f"Ticket {ticket_id} status updated to {statuses[choice]}.")
