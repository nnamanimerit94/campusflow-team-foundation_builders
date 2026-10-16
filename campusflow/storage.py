import json


def save_tickets(tickets):
    """Save all tickets to the JSON file."""

    with open("tickets.json", "w") as file:
        json.dump(tickets, file, indent=4)

   # print("Tickets saved successfully.")