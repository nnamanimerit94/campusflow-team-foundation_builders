# CampusFlow Next
# Follow-up Notes Management


def next_note_id(ticket):
    """Generate the next note ID for a ticket."""

    notes = ticket.get("notes", [])

    highest_number = 0

    for note in notes:
        note_number = int(note["note_id"][1:])

        if note_number > highest_number:
            highest_number = note_number

    return f"N{highest_number + 1:03d}"


def add_note(tickets, ticket_id, author, message):
    """Add a follow-up note to an existing ticket."""

    # Standardize the ticket ID.
    ticket_id = ticket_id.strip().upper()

    # Check that the ticket exists.
    if ticket_id not in tickets:
        raise ValueError("Ticket not found.")

    ticket = tickets[ticket_id]

    # Check whether the ticket can accept notes.
    if ticket["status"] not in ["open", "in_progress"]:
        raise ValueError(
            "Notes can only be added to open or in-progress tickets."
        )

    # Validate the author.
    if not isinstance(author, str) or not author.strip():
        raise ValueError("Author name cannot be empty.")

    # Validate the message.
    if not isinstance(message, str):
        raise ValueError("Note message must be text.")

    message = message.strip()

    if len(message) < 5:
        raise ValueError(
            "Note message must contain at least 5 characters."
        )

    if len(message) > 300:
        raise ValueError(
            "Note message cannot exceed 300 characters."
        )

    # Get the next note ID.
    note_id = next_note_id(ticket)

    # Create the note only after validation succeeds.
    note = {
        "note_id": note_id,
        "author": author.strip(),
        "message": message
    }

    # Create the notes list if it does not exist.
    if "notes" not in ticket:
        ticket["notes"] = []

    # Add the note.
    ticket["notes"].append(note)

    return note


def view_ticket_notes(tickets, ticket_id):
    """Display all notes belonging to a ticket."""

    ticket_id = ticket_id.strip().upper()

    if ticket_id not in tickets:
        print("Ticket not found.")
        return

    ticket = tickets[ticket_id]
    notes = ticket.get("notes", [])

    print(f"\n========== NOTES FOR {ticket_id} ==========")

    if not notes:
        print("No follow-up notes found.")
        return

    # Sort notes by their numeric IDs.
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