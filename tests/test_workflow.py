import unittest
from unittest.mock import patch
from copy import deepcopy

from campusflow.workflow import assign_ticket, update_ticket_status


class TestTicketWorkflow(unittest.TestCase):

    def setUp(self):
        """Create sample tickets before each test."""

        self.tickets = {
            "T001": {
                "id": "T001",
                "title": "Campus Wi-Fi is down",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
                "notes": []
            },
            "T002": {
                "id": "T002",
                "title": "Laptop is faulty",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 3,
                "priority": "medium",
                "status": "open",
                "assigned_to": "John",
                "notes": []
            }
        }

    # ----------------------------------------
    # ASSIGNMENT TESTS
    # ----------------------------------------

    @patch("builtins.input", side_effect=["T001", "Mary"])
    def test_assign_ticket_to_staff(self, mock_input):
        """A valid ticket can be assigned to a staff member."""

        assign_ticket(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["assigned_to"],
            "Mary"
        )

    @patch("builtins.input", side_effect=["T999", "Mary"])
    def test_assign_nonexistent_ticket(self, mock_input):
        """An unknown ticket ID must not change any ticket."""

        original_tickets = deepcopy(self.tickets)

        assign_ticket(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    @patch("builtins.input", side_effect=["T001", "   "])
    def test_assign_ticket_with_blank_staff_name(self, mock_input):
        """A blank staff name must be rejected."""

        original_tickets = deepcopy(self.tickets)

        assign_ticket(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    def test_assign_ticket_when_no_tickets_exist(self):
        """Assignment should be rejected when no tickets exist."""

        empty_tickets = {}

        with patch("builtins.input", return_value="T001"):
            assign_ticket(empty_tickets)

        self.assertEqual(empty_tickets, {})

    # ----------------------------------------
    # STATUS UPDATE TESTS
    # ----------------------------------------

    @patch("builtins.input", side_effect=["T001", "2"])
    def test_update_open_ticket_to_in_progress(self, mock_input):
        """An assigned open ticket can move to in_progress."""

        self.tickets["T001"]["assigned_to"] = "Mary"

        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "in_progress"
        )

    @patch("builtins.input", side_effect=["T001", "3"])
    def test_update_ticket_to_resolved(self, mock_input):
        """An in-progress ticket can be resolved."""

        self.tickets["T001"]["assigned_to"] = "Mary"
        self.tickets["T001"]["status"] = "in_progress"

        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "resolved"
        )

    @patch("builtins.input", side_effect=["T001", "1"])
    def test_reopen_resolved_ticket(self, mock_input):
        """A resolved ticket can be reopened."""

        self.tickets["T001"]["status"] = "resolved"

        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "open"
        )

    @patch("builtins.input", side_effect=["T001", "2"])
    def test_unassigned_ticket_cannot_move_to_in_progress(self, mock_input):
        """An unassigned open ticket must not enter in_progress."""

        original_tickets = deepcopy(self.tickets)

        update_ticket_status(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    @patch("builtins.input", side_effect=["T999", "2"])
    def test_update_nonexistent_ticket(self, mock_input):
        """An unknown ticket ID must not change the collection."""

        original_tickets = deepcopy(self.tickets)

        update_ticket_status(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    @patch("builtins.input", side_effect=["T001", "9"])
    def test_invalid_status_choice(self, mock_input):
        """An invalid menu choice must not change ticket data."""

        original_tickets = deepcopy(self.tickets)

        update_ticket_status(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    @patch("builtins.input", side_effect=["T001", "3"])
    def test_open_ticket_cannot_skip_to_resolved(self, mock_input):
        """An open ticket must not skip the in_progress state."""

        original_tickets = deepcopy(self.tickets)

        update_ticket_status(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    @patch("builtins.input", side_effect=["T001", "2"])
    def test_resolved_ticket_cannot_move_directly_to_in_progress(
        self, mock_input
    ):
        """A resolved ticket must be reopened before work resumes."""

        self.tickets["T001"]["status"] = "resolved"
        original_tickets = deepcopy(self.tickets)

        update_ticket_status(self.tickets)

        self.assertEqual(self.tickets, original_tickets)

    def test_status_update_when_no_tickets_exist(self):
        """Status updates must be rejected for an empty collection."""

        empty_tickets = {}

        with patch("builtins.input", return_value="T001"):
            update_ticket_status(empty_tickets)

        self.assertEqual(empty_tickets, {})


if __name__ == "__main__":
    unittest.main()