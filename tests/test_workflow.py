import unittest
from unittest.mock import patch
from campusflow.workflow import update_ticket_status, view_work_queue


class TestWorkflow(unittest.TestCase):

    # Sample tickets for testing
    def setUp(self):
        self.tickets = {
            "T001": {
                "id": "T001",
                "title": "Wi-Fi is not working",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None
            },
            "T002": {
                "id": "T002",
                "title": "Laptop problem",
                "category": "Hardware",
                "urgency": "medium",
                "affected_users": 3,
                "priority": "medium",
                "status": "open",
                "assigned_to": None
            }
        }

    # Test 1: Update a ticket to in progress
    @patch("builtins.input", side_effect=["T001", "2"])
    def test_update_ticket_status(self, mock_input):
        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "in_progress"
        )

    # Test 2: Resolve a ticket
    @patch("builtins.input", side_effect=["T001", "3"])
    def test_resolve_ticket(self, mock_input):
        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "resolved"
        )

    # Test 3: Reject an invalid ticket ID
    @patch("builtins.input", side_effect=["T999"])
    def test_invalid_ticket_id(self, mock_input):
        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "open"
        )

    # Test 4: Reject an invalid status choice
    @patch("builtins.input", side_effect=["T001", "9"])
    def test_invalid_status_choice(self, mock_input):
        update_ticket_status(self.tickets)

        self.assertEqual(
            self.tickets["T001"]["status"],
            "open"
        )

    # Test 5: Handle an empty ticket dictionary
    def test_empty_tickets(self):
        tickets = {}

        update_ticket_status(tickets)

        self.assertEqual(len(tickets), 0)

    # Test 6: Work queue displays unresolved tickets
    @patch("builtins.print")
    def test_view_work_queue(self, mock_print):
        view_work_queue(self.tickets)

        output = " ".join(
            str(call) for call in mock_print.call_args_list
        )

        self.assertIn("T001", output)
        self.assertIn("T002", output)

    # Test 7: Work queue excludes resolved tickets
    @patch("builtins.print")
    def test_work_queue_excludes_resolved_tickets(self, mock_print):
        self.tickets["T002"]["status"] = "resolved"

        view_work_queue(self.tickets)

        output = " ".join(
            str(call) for call in mock_print.call_args_list
        )

        self.assertIn("T001", output)
        self.assertNotIn("T002", output)

    # Test 8: Work queue displays higher priorities first
    @patch("builtins.print")
    def test_work_queue_priority_order(self, mock_print):
        view_work_queue(self.tickets)

        output = " ".join(
            str(call) for call in mock_print.call_args_list
        )

        critical_position = output.find("critical")
        medium_position = output.find("medium")

        self.assertLess(critical_position, medium_position)


if __name__ == "__main__":
    unittest.main()