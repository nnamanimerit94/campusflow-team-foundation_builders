import unittest
from unittest.mock import patch

from campusflow.tickets import (
    create_ticket,
    view_all_tickets,
    assign_ticket
)


class TestTickets(unittest.TestCase):

    # Test 1: Check if a ticket can be created
    @patch("builtins.input", side_effect=[
        "Campus Wi-Fi is down",
        "1",
        "3",
        "15"
    ])
    def test_create_ticket(self, mock_input):
        tickets = {}

        create_ticket(tickets)

        self.assertEqual(len(tickets), 1)
        self.assertIn("T001", tickets)
        self.assertEqual(
            tickets["T001"]["title"],
            "Campus Wi-Fi is down"
        )
        self.assertEqual(tickets["T001"]["status"], "open")

    # Test 2: Check if a ticket has the correct category
    @patch("builtins.input", side_effect=[
        "Laptop problem",
        "2",
        "2",
        "3"
    ])
    def test_ticket_category(self, mock_input):
        tickets = {}

        create_ticket(tickets)

        self.assertEqual(
            tickets["T001"]["category"],
            "Hardware"
        )

    # Test 3: Check if a ticket has the correct priority
    @patch("builtins.input", side_effect=[
        "Internet problem",
        "1",
        "3",
        "15"
    ])
    def test_ticket_priority(self, mock_input):
        tickets = {}

        create_ticket(tickets)

        self.assertEqual(
            tickets["T001"]["priority"],
            "critical"
        )

    # Test 4: Check if an invalid ticket title is rejected
    @patch("builtins.input", side_effect=[""])
    def test_empty_ticket_title(self, mock_input):
        tickets = {}

        create_ticket(tickets)

        self.assertEqual(len(tickets), 0)

    # Test 5: Check if a ticket can be assigned
    @patch("builtins.input", side_effect=["T001", "John"])
    def test_assign_ticket(self, mock_input):
        tickets = {
            "T001": {
                "id": "T001",
                "title": "Wi-Fi problem",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None
            }
        }

        assign_ticket(tickets)

        self.assertEqual(
            tickets["T001"]["assigned_to"],
            "John"
        )

    # Test 6: Check if an invalid ticket ID is rejected
    @patch("builtins.input", side_effect=["T999"])
    def test_assign_invalid_ticket(self, mock_input):
        tickets = {}

        assign_ticket(tickets)

        self.assertEqual(len(tickets), 0)

    # Test 7: Check viewing tickets when the dictionary is empty
    def test_view_empty_tickets(self):
        tickets = {}

        view_all_tickets(tickets)

        self.assertEqual(len(tickets), 0)

    # Test 8: Check if viewing tickets preserves ticket data
    def test_view_tickets(self):
        tickets = {
            "T001": {
                "id": "T001",
                "title": "Wi-Fi problem",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None
            }
        }

        view_all_tickets(tickets)

        self.assertIn("T001", tickets)
        self.assertEqual(
            tickets["T001"]["title"],
            "Wi-Fi problem"
        )


if __name__ == "__main__":
    unittest.main()