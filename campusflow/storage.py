# CampusFlow Next - Ticket Storage

import json
import os

from campusflow.tickets import calculate_priority


# Get the path of tickets.json in the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TICKET_FILE = os.path.join(BASE_DIR, "tickets.json")


# Validate one ticket
def validate_ticket(ticket_id, ticket):
    """Check whether a ticket has valid data."""

    # Check that the ticket is a dictionary
    if not isinstance(ticket, dict):
        raise ValueError("Ticket data must be a dictionary.")

    # Check the required ticket fields
    required_fields = [
        "id",
        "title",
        "category",
        "urgency",
        "affected_users",
        "priority",
        "status",
        "assigned_to",
        "notes"
    ]

    for field in required_fields:
        if field not in ticket:
            raise ValueError(f"Ticket {ticket_id} is missing {field}.")

    # Check the ticket ID
    if ticket["id"] != ticket_id:
        raise ValueError(f"Ticket ID mismatch for {ticket_id}.")

    if not isinstance(ticket_id, str):
        raise ValueError("Ticket ID must be a string.")

    if len(ticket_id) < 2 or not ticket_id.startswith("T"):
        raise ValueError(f"Invalid ticket ID: {ticket_id}.")

    if not ticket_id[1:].isdigit():
        raise ValueError(f"Invalid ticket ID: {ticket_id}.")

    # Check the title
    if not isinstance(ticket["title"], str) or not ticket["title"].strip():
        raise ValueError(f"Ticket {ticket_id} has an invalid title.")

    # Check the category
    valid_categories = ["Network", "Hardware", "Software", "Other"]

    if ticket["category"] not in valid_categories:
        raise ValueError(f"Ticket {ticket_id} has an invalid category.")

    # Check urgency
    valid_urgencies = ["low", "medium", "high"]

    if ticket["urgency"] not in valid_urgencies:
        raise ValueError(f"Ticket {ticket_id} has an invalid urgency.")

    # Check affected users
    affected_users = ticket["affected_users"]

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError(
            f"Ticket {ticket_id} must have a positive integer for affected users."
        )

    # Check priority consistency
    expected_priority = calculate_priority(
        ticket["urgency"],
        affected_users
    )

    if ticket["priority"] != expected_priority:
        raise ValueError(f"Ticket {ticket_id} has an inconsistent priority.")

    # Check status
    valid_statuses = ["open", "in_progress", "resolved"]

    if ticket["status"] not in valid_statuses:
        raise ValueError(f"Ticket {ticket_id} has an invalid status.")

    # Check assignment
    assigned_to = ticket["assigned_to"]

    if assigned_to is not None:
        if not isinstance(assigned_to, str) or not assigned_to.strip():
            raise ValueError(f"Ticket {ticket_id} has an invalid assignment.")

    # Check notes
    if not isinstance(ticket["notes"], list):
        raise ValueError(f"Ticket {ticket_id} notes must be a list.")

    note_ids = []

    for note in ticket["notes"]:

        if not isinstance(note, dict):
            raise ValueError(f"Ticket {ticket_id} contains an invalid note.")

        required_note_fields = ["note_id", "author", "message"]

        for field in required_note_fields:
            if field not in note:
                raise ValueError(
                    f"A note in ticket {ticket_id} is missing {field}."
                )

        note_id = note["note_id"]
        author = note["author"]
        message = note["message"]

        if not isinstance(note_id, str):
            raise ValueError("Note ID must be a string.")

        if len(note_id) < 2 or not note_id.startswith("N"):
            raise ValueError(f"Invalid note ID: {note_id}.")

        if not note_id[1:].isdigit():
            raise ValueError(f"Invalid note ID: {note_id}.")

        if note_id in note_ids:
            raise ValueError(
                f"Ticket {ticket_id} contains duplicate note IDs."
            )

        note_ids.append(note_id)

        if not isinstance(author, str) or not author.strip():
            raise ValueError("Note author cannot be empty.")

        if not isinstance(message, str):
            raise ValueError("Note message must be text.")

        if not 5 <= len(message.strip()) <= 300:
            raise ValueError(
                "Note message must contain 5 to 300 characters."
            )

    return True


# Validate the complete ticket collection
def validate_tickets(tickets):
    """Validate every ticket before accepting the collection."""

    if not isinstance(tickets, dict):
        raise ValueError("The ticket collection must be a dictionary.")

    for ticket_id, ticket in tickets.items():
        validate_ticket(ticket_id, ticket)

    return True


# Create the JSON file if it does not exist
def create_ticket_file():
    """Create an empty JSON file when necessary."""

    if not os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)


# Load tickets from JSON
def load_tickets(path=TICKET_FILE):
    """
    Load and validate tickets from JSON.

    Returns a dictionary of dictionaries.
    Raises an error if the file contains invalid data.
    """

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=4)

        return {}

    try:
        with open(path, "r", encoding="utf-8") as file:
            loaded_tickets = json.load(file)

    except json.JSONDecodeError as error:
        raise ValueError("The tickets JSON file contains invalid JSON.") from error

    # Validate everything before returning the loaded collection
    validate_tickets(loaded_tickets)

    return loaded_tickets


# Save tickets to JSON
def save_tickets(tickets, path=TICKET_FILE):
    """Validate and save the ticket collection."""

    # Never save an invalid collection
    validate_tickets(tickets)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)

    print("Tickets saved successfully.")