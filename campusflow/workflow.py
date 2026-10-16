def update_ticket_status(tickets):
    """Update the status of a support ticket."""

#view work queue by priority
def view_work_queue(tickets):
    """Display unresolved tickets in priority order."""

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
    # Select tickets that are not resolved or closed
    work_queue = []

    for ticket in tickets.values():
        if ticket["status"] in ["open", "in_progress"]:
            work_queue.append(ticket)

    if not work_queue:
        print("There are no tickets in the work queue.")
        return

    # Define the priority order
    priority_order = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    # Sort tickets by priority
    work_queue.sort(
        key=lambda ticket: priority_order.get(ticket["priority"], 5)
    )

    # Display the work queue
    print("\n========== WORK QUEUE ==========")

    for ticket in work_queue:
        print("------------------------------")
        print("Ticket ID:", ticket["id"])
        print("Title:", ticket["title"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])
        print("Assigned To:", ticket["assigned_to"])
def view_reports(tickets):
    """Display a summary of all support tickets."""

    print("\n========== TICKET REPORTS ==========")

    if not tickets:
        print("No tickets available for reporting.")
        return

    # Count the total number of tickets
    total_tickets = len(tickets)

    print("Total Tickets:", total_tickets)

    # Count tickets by status
    open_tickets = 0
    in_progress_tickets = 0
    resolved_tickets = 0
    closed_tickets = 0

    for ticket in tickets.values():
        if ticket["status"] == "open":
            open_tickets += 1
        elif ticket["status"] == "in_progress":
            in_progress_tickets += 1
        elif ticket["status"] == "resolved":
            resolved_tickets += 1
        elif ticket["status"] == "closed":
            closed_tickets += 1

    print("\n--- Tickets by Status ---")
    print("Open:", open_tickets)
    print("In Progress:", in_progress_tickets)
    print("Resolved:", resolved_tickets)
    print("Closed:", closed_tickets)

    # Count tickets by priority
    critical_tickets = 0
    high_tickets = 0
    medium_tickets = 0
    low_tickets = 0

    for ticket in tickets.values():
        if ticket["priority"] == "critical":
            critical_tickets += 1
        elif ticket["priority"] == "high":
            high_tickets += 1
        elif ticket["priority"] == "medium":
            medium_tickets += 1
        elif ticket["priority"] == "low":
            low_tickets += 1

    print("\n--- Tickets by Priority ---")
    print("Critical:", critical_tickets)
    print("High:", high_tickets)
    print("Medium:", medium_tickets)
    print("Low:", low_tickets)

    print("====================================")
