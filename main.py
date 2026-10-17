# CampusFlow Next
# Campus Helpdesk Management System

from campusflow.tickets import (
    create_ticket,
    view_all_tickets,
    view_student_tickets,
    assign_ticket
)

from campusflow.search import (
    search_tickets,
    display_search_results
)

from campusflow import workflow
from campusflow import storage
from campusflow import reports


# Load tickets from the JSON file
def load_tickets():
    """Load tickets when the application starts."""

    try:
        tickets = storage.load_tickets()
        print("Tickets loaded successfully.")
        return tickets

    except FileNotFoundError:
        print("Ticket file not found. Starting with an empty collection.")
        return {}

    except (ValueError, OSError) as error:
        #print("Could not load tickets:", error)
        return {}


# Save tickets to the JSON file
def save_tickets(tickets):
    """Save tickets to the JSON file."""

    try:
        storage.save_tickets(tickets)
        print("Tickets saved successfully.")

    except (OSError, ValueError) as error:
        print("Could not save tickets:", error)


# Update ticket status
def update_ticket_status(tickets):
    """Ask for the ticket ID and new status."""

    print("\n========== UPDATE TICKET STATUS ==========")

    if not tickets:
        print("No tickets available.")
        return

    # Ask for the ticket ID only once.
    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    print("Current status:", tickets[ticket_id]["status"])

    print("\nSelect the new status:")
    print("1. In Progress")
    print("2. Resolved")
    print("3. Reopen ticket")

    choice = input("Enter your choice: ").strip()

    statuses = {
        "1": "in_progress",
        "2": "resolved",
        "3": "open"
    }

    if choice not in statuses:
        print("Invalid choice. Status was not changed.")
        return

    new_status = statuses[choice]

    try:
        # Pass the ticket ID and new status to workflow.py.
        workflow.update_ticket_status(
            tickets,
            ticket_id,
            new_status
        )

        # Save after a successful status update.
        save_tickets(tickets)

    except ValueError as error:
        print("Could not update ticket:", error)





# Display the Open Work Queue
def view_work_queue(tickets):
    """Display open tickets in priority order."""

    if not tickets:
        print("No tickets available.")
        return

    # Priority order required by the assignment.
    priority_order = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }

    # Only open tickets should appear in this queue.
    open_tickets = {}

    for ticket_id, ticket in tickets.items():
        if ticket["status"] == "open":
            open_tickets[ticket_id] = ticket

    if not open_tickets:
        print("There are no open tickets in the work queue.")
        return

    # Sort by priority, then by numeric ticket ID.
    sorted_tickets = sorted(
        open_tickets.items(),
        key=lambda item: (
            priority_order.get(item[1]["priority"], 5),
            int(item[0][1:])
        )
    )

    print("\n========== OPEN WORK QUEUE ==========")

    for ticket_id, ticket in sorted_tickets:
        print("-" * 40)
        print("Ticket ID:", ticket_id)
        print("Title:", ticket["title"])
        print("Priority:", ticket["priority"])
        print("Status:", ticket["status"])
        print("Assigned To:", ticket["assigned_to"])

    print("-" * 40)


# Search tickets
def search_tickets_menu(tickets):
    """Search tickets using a title and optional filters."""

    print("\n========== SEARCH TICKETS ==========")

    # Search by title
    title = input(
        "Enter a title or part of a title "
        "(press Enter to skip): "
    ).strip()

    # Select category
    while True:
        print("\nSelect category:")
        print("1. Network")
        print("2. Hardware")
        print("3. Software")
        print("4. Other")
        print("5. All categories")

        category_choice = input("Enter your choice: ").strip()

        categories = {
            "1": "Network",
            "2": "Hardware",
            "3": "Software",
            "4": "Other",
            "5": ""
        }

        if category_choice in categories:
            category = categories[category_choice]
            break

        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

    # Select status
    while True:
        print("\nSelect status:")
        print("1. Open")
        print("2. In Progress")
        print("3. Resolved")
        print("4. All statuses")

        status_choice = input("Enter your choice: ").strip()

        statuses = {
            "1": "open",
            "2": "in_progress",
            "3": "resolved",
            "4": ""
        }

        if status_choice in statuses:
            status = statuses[status_choice]
            break

        print("Invalid choice. Please select 1, 2, 3, or 4.")

    # Select priority
    while True:
        print("\nSelect priority:")
        print("1. Critical")
        print("2. High")
        print("3. Medium")
        print("4. Low")
        print("5. All priorities")

        priority_choice = input("Enter your choice: ").strip()

        priorities = {
            "1": "critical",
            "2": "high",
            "3": "medium",
            "4": "low",
            "5": ""
        }

        if priority_choice in priorities:
            priority = priorities[priority_choice]
            break

        print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

    # Perform the search
    results = search_tickets(
        tickets,
        title=title,
        category=category,
        status=status,
        priority=priority
    )

    # Display matching tickets
    display_search_results(results)






# Add a follow-up note
def add_follow_up_note(tickets):
    """Collect information and add a follow-up note."""

    from campusflow.notes import add_note

    print("\n========== ADD FOLLOW-UP NOTE ==========")

    ticket_id = input("Enter ticket ID: ").strip().upper()
    author = input("Enter your name or staff label: ").strip()
    message = input("Enter your note: ").strip()

    try:
        note = add_note(
            tickets,
            ticket_id,
            author,
            message
        )

        print("\nFollow-up note added successfully!")
        print("Ticket ID:", ticket_id)
        print("Note ID:", note["note_id"])

        save_tickets(tickets)

    except ValueError as error:
        print("Could not add note:", error)






# View follow-up notes
def view_ticket_notes(tickets):
    """Display the notes attached to a ticket."""

    print("\n========== VIEW TICKET NOTES ==========")

    ticket_id = input("Enter ticket ID: ").strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    notes = tickets[ticket_id].get("notes", [])

    if not notes:
        print("This ticket has no follow-up notes.")
        return

    # Display notes in note ID order.
    sorted_notes = sorted(
        notes,
        key=lambda note: int(note["note_id"][1:])
    )

    for note in sorted_notes:
        print("-" * 40)
        print("Note ID:", note["note_id"])
        print("Author:", note["author"])
        print("Message:", note["message"])

    print("-" * 40)


# Display reports
def view_reports(tickets):
    """Display ticket statistics."""

    print("\n========== TICKET REPORTS ==========")

    try:
        reports.generate_report(tickets)

    except AttributeError:
        print(
            "The report module does not yet contain "
            "a generate_report() function."
        )


# Student menu
def student_menu(tickets):
    """Display the student menu."""

    while True:
        print("\n========== STUDENT MENU ==========")
        print("1. Create a support ticket")
        print("2. View tickets")
        print("3. Search tickets")
        print("4. Add follow-up note")
        print("5. View ticket notes")
        print("6. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_ticket(tickets)
            save_tickets(tickets)

        elif choice == "2":
            view_student_tickets(tickets)

        elif choice == "3":
            search_tickets_menu(tickets)

        elif choice == "4":
            add_follow_up_note(tickets)

        elif choice == "5":
            view_ticket_notes(tickets)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


# Admin menu
def admin_menu(tickets):
    """Display the administrator menu."""

    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. View all tickets")
        print("2. Assign ticket")
        print("3. Update ticket status")
        print("4. View Open Work Queue")
        print("5. View reports")
        print("6. Search tickets")
        print("7. Add follow-up note")
        print("8. View ticket notes")
        print("9. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_all_tickets(tickets)

        elif choice == "2":
            assign_ticket(tickets)
            save_tickets(tickets)

        elif choice == "3":
            update_ticket_status(tickets)
            
        elif choice == "4":
            view_work_queue(tickets)

        elif choice == "5":
            view_reports(tickets)

        elif choice == "6":
            search_tickets_menu(tickets)

        elif choice == "7":
            add_follow_up_note(tickets)

        elif choice == "8":
            view_ticket_notes(tickets)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")


# Main application
def main():
    """Start the CampusFlow application."""

    print("====================================")
    print(" Welcome to CampusFlow Next")
    print(" Campus Helpdesk Management System")
    print("====================================")

    tickets = load_tickets()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Admin")
        print("2. Student")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            admin_menu(tickets)

        elif choice == "2":
            student_menu(tickets)

        elif choice == "3":
            print("Thank you for using CampusFlow Next!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
