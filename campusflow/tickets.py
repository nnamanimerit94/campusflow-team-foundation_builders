def view_all_tickets(tickets):
    """Display all support tickets."""

    if not tickets:
        print("No tickets found.")
        return

    print("\n========== ALL SUPPORT TICKETS ==========\n")
    for ticket_id, ticket in tickets.items():
        display_ticket(ticket_id, ticket)

    
#display ticket helper function
def display_ticket(ticket_id, ticket):
    """Display all support tickets."""
    print(f"Ticket ID: {ticket_id}")
    print(f"Title: {ticket['title']}")
    print(f"Category: {ticket['category']}")
    print(f"Urgency: {ticket['urgency']}")
    print(f"Affected Users: {ticket['affected_users']}")
    print(f"Priority: {ticket['priority']}")
    print(f"Status: {ticket['status']}")
    print(f"Assigned To: {ticket['assigned_to']}")
    print("-" * 40)


def calculate_priority(urgency, affected_users):
    if urgency == "high" and affected_users >= 10:
        return "critical"
    elif urgency == "high" or affected_users >= 10:
        return "high"
    elif urgency == "medium" or affected_users >= 3:
        return "medium"
    else:
        return "low"
    


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





#create ticket code
def create_ticket(tickets):
    """Create a new support ticket."""

    print("\n========== CREATE SUPPORT TICKET ==========")

    # Get ticket details from the student
    title = input("Enter ticket title: ").strip()

    if not title:
        print("Ticket title cannot be empty.")
        return

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

    try:
        affected_users = int(
            input("Enter the number of affected users: ")
        )

        if affected_users < 1:
            print("The number of affected users must be at least 1.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    # Generate a unique ticket ID
    ticket_number = len(tickets) + 1
    ticket_id = f"T{ticket_number:03d}"

    while ticket_id in tickets:
        ticket_number += 1
        ticket_id = f"T{ticket_number:03d}"

    priority = calculate_priority(urgency, affected_users)
    # Create the ticket dictionary
    ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }

    # Add the ticket to the main tickets dictionary
    tickets[ticket_id] = ticket

    print("\nTicket created successfully!")
    print("Ticket ID:", ticket_id)
    print("Title:", title)
    print("Category:", category)
    print("Priority:", priority)
    print("Status: open")






#student view tickets
def view_student_tickets(tickets):
    """Display all tickets for students."""

    if not tickets:
        print("\nNo tickets are available.")
        return

    print("\n========== VIEW TICKETS ==========")

    for ticket_id, ticket in tickets.items():
        print("----------------------------------")
        print("Ticket ID:", ticket_id)
        print("Title:", ticket["title"])
        print("Category:", ticket["category"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])

    print("----------------------------------")