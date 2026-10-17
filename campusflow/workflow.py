# CampusFlow Next
# Ticket Workflow Management

def update_ticket_status(tickets, ticket_id, new_status):
    """Change a ticket's status to the status selected by the admin."""

    ticket_id = ticket_id.strip().upper()

    # Check that the ticket exists.
    if ticket_id not in tickets:
        raise ValueError("Ticket not found.")

    # Check that the selected status is valid.
    valid_statuses = ["open", "in_progress", "resolved"]

    if new_status not in valid_statuses:
        raise ValueError("Invalid status selected.")

    # Change the status directly to the user's selection.
    tickets[ticket_id]["status"] = new_status

    print(f"Ticket {ticket_id} status changed to {new_status}.")

def view_work_queue(tickets):
    """
    Display OPEN tickets in priority order.

    Priority order:
    critical -> high -> medium -> low

    Tickets with equal priority are ordered by their
    numeric ticket ID, from lowest to highest.
    """

    if not tickets:
        print("No tickets available.")
        return

    # Define the priority order.
    priority_order = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    # Collect only open tickets.
    work_queue = []

    for ticket_id, ticket in tickets.items():

        if ticket["status"] == "open":
            work_queue.append((ticket_id, ticket))

    if not work_queue:
        print("There are no open tickets in the work queue.")
        return

    # Sort by priority and then numeric ticket ID.
    work_queue.sort(
        key=lambda item: (
            priority_order[item[1]["priority"]],
            int(item[0][1:])
        )
    )

    # Display the work queue.
    print("\n========== OPEN WORK QUEUE ==========")

    for ticket_id, ticket in work_queue:

        print("-" * 40)
        print("Ticket ID:", ticket_id)
        print("Title:", ticket["title"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])
        print("Assigned To:", ticket["assigned_to"])

    print("-" * 40)