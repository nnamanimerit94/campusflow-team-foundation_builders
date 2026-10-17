# CampusFlow Next - Ticket Management


# Calculate ticket priority
def calculate_priority(urgency, affected_users):
    """Calculate ticket priority using the assignment rules."""

    if urgency == "high" and affected_users >= 10:
        return "critical"

    elif urgency == "high" or affected_users >= 10:
        return "high"

    elif urgency == "medium" or affected_users >= 3:
        return "medium"

    else:
        return "low"


# Validate ticket information
def validate_ticket(title, category, urgency, affected_users):
    """Check whether the ticket information is valid."""

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Ticket title cannot be empty.")

    if category not in ["Network", "Hardware", "Software", "Other"]:
        raise ValueError("Invalid ticket category.")

    if urgency not in ["low", "medium", "high"]:
        raise ValueError("Invalid urgency.")

    # bool is a subclass of int in Python, so reject it explicitly.
    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError(
            "Affected users must be a positive whole number."
        )


# Generate the next ticket ID
def next_ticket_id(tickets):
    """Generate a unique ticket ID."""

    highest_number = 0

    for ticket_id in tickets:
        if (
            isinstance(ticket_id, str)
            and ticket_id.startswith("T")
            and ticket_id[1:].isdigit()
        ):
            number = int(ticket_id[1:])

            if number > highest_number:
                highest_number = number

    return f"T{highest_number + 1:03d}"


# Display all tickets
def view_all_tickets(tickets):
    """Display all support tickets."""

    if not tickets:
        print("\nNo tickets found.")
        return

    print("\n========== ALL SUPPORT TICKETS ==========\n")

    for ticket_id, ticket in tickets.items():
        print(f"Ticket ID: {ticket_id}")
        print(f"Title: {ticket['title']}")
        print(f"Category: {ticket['category']}")
        print(f"Urgency: {ticket['urgency']}")
        print(f"Affected Users: {ticket['affected_users']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"Assigned To: {ticket['assigned_to']}")
        print("-" * 40)


# Assign a ticket to a staff member
def assign_ticket(tickets):
    """Assign a ticket to a staff member."""

    if not tickets:
        print("\nNo tickets available for assignment.")
        return

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    ticket = tickets[ticket_id]

    # A resolved ticket cannot be reassigned.
    if ticket["status"] == "resolved":
        print("A resolved ticket must be reopened before reassignment.")
        return

    staff_name = input("Enter staff member's name: ").strip()

    if not staff_name:
        print("Staff name cannot be empty.")
        return

    # Change the ticket only after validation.
    ticket["assigned_to"] = staff_name

    print(f"Ticket {ticket_id} has been assigned to {staff_name}.")


# Create a new support ticket
def create_ticket(tickets):
    """Collect information and create a support ticket."""

    print("\n========== CREATE SUPPORT TICKET ==========")

    # Get the ticket title.
    title = input("Enter ticket title: ").strip()

    if not title:
        print("Ticket title cannot be empty.")
        return

    # Get the category.
    print("\nSelect a category:")
    print("1. Network")
    print("2. Hardware")
    print("3. Software")
    print("4. Other")

    category_choice = input("Enter your choice: ").strip()

    categories = {
        "1": "Network",
        "2": "Hardware",
        "3": "Software",
        "4": "Other"
    }

    if category_choice not in categories:
        print("Invalid category.")
        return

    category = categories[category_choice]

    # Get the urgency.
    print("\nSelect urgency:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    urgency_choice = input("Enter your choice: ").strip()

    urgencies = {
        "1": "low",
        "2": "medium",
        "3": "high"
    }

    if urgency_choice not in urgencies:
        print("Invalid urgency.")
        return

    urgency = urgencies[urgency_choice]

    # Get the number of affected users.
    affected_users_input = input(
        "Enter the number of affected users: "
    ).strip()

    try:
        affected_users = int(affected_users_input)

    except ValueError:
        print("Please enter a valid whole number.")
        return

    # Validate the information before creating the ticket.
    try:
        validate_ticket(
            title,
            category,
            urgency,
            affected_users
        )

    except ValueError as error:
        print(error)
        return

    # Generate a unique ticket ID.
    ticket_id = next_ticket_id(tickets)

    # Calculate priority using the assignment rules.
    priority = calculate_priority(urgency, affected_users)

    # Create the ticket.
    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None,
        "notes": []
    }

    # Add the ticket to the collection.
    tickets[ticket_id] = ticket

    print("\nTicket created successfully!")
    print(f"Ticket ID: {ticket_id}")
    print(f"Title: {title}")
    print(f"Category: {category}")
    print(f"Priority: {priority}")
    print("Status: open")


# Display tickets for students
def view_student_tickets(tickets):
    """Display ticket information for students."""

    if not tickets:
        print("\nNo tickets are available.")
        return

    print("\n========== VIEW TICKETS ==========")

    for ticket_id, ticket in tickets.items():
        print("-" * 35)
        print(f"Ticket ID: {ticket_id}")
        print(f"Title: {ticket['title']}")
        print(f"Category: {ticket['category']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")

    print("-" * 35)