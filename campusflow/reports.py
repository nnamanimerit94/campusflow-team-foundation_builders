# CampusFlow Next - Ticket Reports


# View ticket reports
def view_reports(tickets):
    """Display statistics about the campus support tickets."""

    print("\n========================================")
    print("          CAMPUSFLOW REPORTS")
    print("========================================")

    # Calculate the total number of tickets
    total_tickets = len(tickets)

    print(f"\nTotal tickets: {total_tickets}")

    # Prepare counters for ticket statuses
    status_counts = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0
    }

    # Prepare counters for ticket priorities
    priority_counts = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    # Prepare counters for ticket categories
    category_counts = {
        "Network": 0,
        "Hardware": 0,
        "Software": 0,
        "Other": 0
    }

    # Count the tickets
    for ticket in tickets.values():

        status = ticket["status"]
        priority = ticket["priority"]
        category = ticket["category"]

        # Count ticket status
        if status in status_counts:
            status_counts[status] += 1

        # Count ticket priority
        if priority in priority_counts:
            priority_counts[priority] += 1

        # Count ticket category
        if category in category_counts:
            category_counts[category] += 1

    # Display tickets by status
    print("\n--- TICKETS BY STATUS ---")

    for status, count in status_counts.items():
        print(f"{status.replace('_', ' ').title()}: {count}")

    # Display tickets by priority
    print("\n--- TICKETS BY PRIORITY ---")

    for priority, count in priority_counts.items():
        print(f"{priority.title()}: {count}")

    # Display tickets by category
    print("\n--- TICKETS BY CATEGORY ---")

    for category, count in category_counts.items():
        print(f"{category}: {count}")

    # Calculate unresolved tickets
    unresolved_tickets = (
        status_counts["open"]
        + status_counts["in_progress"]
    )

    # Calculate resolved tickets
    resolved_tickets = status_counts["resolved"]

    print("\n--- RESOLUTION SUMMARY ---")

    print(f"Unresolved tickets: {unresolved_tickets}")
    print(f"Resolved tickets: {resolved_tickets}")

    # Calculate the resolution percentage
    if total_tickets == 0:
        resolution_percentage = 0
    else:
        resolution_percentage = (
            resolved_tickets / total_tickets
        ) * 100

    print(f"Resolution percentage: {resolution_percentage:.2f}%")

    print("\n========================================")



    # CampusFlow Next
# Ticket Reports


def generate_report(tickets):
    """Display statistics about campus support tickets."""

    print("\n========== TICKET REPORTS ==========")

    # Count all tickets.
    total_tickets = len(tickets)

    # Prepare the counters.
    status_counts = {
        "open": 0,
        "in_progress": 0,
        "resolved": 0
    }

    priority_counts = {
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    category_counts = {
        "Network": 0,
        "Hardware": 0,
        "Software": 0,
        "Other": 0
    }

    # Count tickets by status, priority and category.
    for ticket in tickets.values():

        status = ticket["status"]
        priority = ticket["priority"]
        category = ticket["category"]

        if status in status_counts:
            status_counts[status] += 1

        if priority in priority_counts:
            priority_counts[priority] += 1

        if category in category_counts:
            category_counts[category] += 1

    # Calculate resolved and unresolved tickets.
    resolved_tickets = status_counts["resolved"]

    unresolved_tickets = (
        status_counts["open"]
        + status_counts["in_progress"]
    )

    # Calculate the resolution percentage.
    if total_tickets == 0:
        resolution_percentage = 0
    else:
        resolution_percentage = (
            resolved_tickets / total_tickets
        ) * 100

    # Display the total.
    print("\nTotal tickets:", total_tickets)

    # Display status statistics.
    print("\n--- Tickets by Status ---")

    print("Open:", status_counts["open"])
    print("In Progress:", status_counts["in_progress"])
    print("Resolved:", status_counts["resolved"])

    # Display priority statistics.
    print("\n--- Tickets by Priority ---")

    print("Critical:", priority_counts["critical"])
    print("High:", priority_counts["high"])
    print("Medium:", priority_counts["medium"])
    print("Low:", priority_counts["low"])

    # Display category statistics.
    print("\n--- Tickets by Category ---")

    print("Network:", category_counts["Network"])
    print("Hardware:", category_counts["Hardware"])
    print("Software:", category_counts["Software"])
    print("Other:", category_counts["Other"])

    # Display resolution statistics.
    print("\n--- Resolution Summary ---")

    print("Unresolved tickets:", unresolved_tickets)
    print("Resolved tickets:", resolved_tickets)
    print(f"Resolution percentage: {resolution_percentage:.2f}%")

    print("\n====================================")