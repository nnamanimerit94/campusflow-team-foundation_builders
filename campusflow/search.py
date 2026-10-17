# CampusFlow Next - Ticket Search


def search_tickets(
    tickets,
    title="",
    category="",
    status="",
    priority=""
):
    """Search tickets using a title and optional filters."""

    results = {}

    title = title.strip().casefold()
    category = category.strip().casefold()
    status = status.strip().casefold()
    priority = priority.strip().casefold()

    for ticket_id, ticket in tickets.items():

        # Search by title.
        if title and title not in ticket["title"].casefold():
            continue

        # Filter by category.
        if category and category != ticket["category"].casefold():
            continue

        # Filter by status.
        if status and status != ticket["status"].casefold():
            continue

        # Filter by priority.
        if priority and priority != ticket["priority"].casefold():
            continue

        results[ticket_id] = ticket

    return results


def display_search_results(results):
    """Display the matching tickets."""

    if not results:
        print("\nNo matching tickets found.")
        return

    print("\n========== SEARCH RESULTS ==========")

    for ticket_id, ticket in results.items():
        print("-" * 40)
        print("Ticket ID:", ticket_id)
        print("Title:", ticket["title"])
        print("Category:", ticket["category"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])
        print("Assigned To:", ticket["assigned_to"])

    print("-" * 40)