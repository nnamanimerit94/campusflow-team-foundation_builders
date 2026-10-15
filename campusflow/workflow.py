
#view work queue by priority
def view_work_queue(tickets):
    """Display unresolved tickets in priority order."""

    if not tickets:
        print("No tickets available.")
        return

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