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