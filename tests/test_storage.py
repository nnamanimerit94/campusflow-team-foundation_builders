import json
import os
import tempfile
import unittest
from copy import deepcopy

from campusflow.storage import save_tickets, load_tickets


class TestTicketStorage(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and sample tickets."""

        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(
            self.temp_dir.name,
            "tickets.json"
        )

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
                "status": "in_progress",
                "assigned_to": "John",
                "notes": [
                    {
                        "note_id": "N001",
                        "author": "Mentor A",
                        "message": "Laptop inspection started"
                    }
                ]
            }
        }

    def tearDown(self):
        """Remove the temporary directory after each test."""

        self.temp_dir.cleanup()

    # ----------------------------------------
    # SAVING TESTS
    # ----------------------------------------

    def test_save_tickets_creates_json_file(self):
        """Saving tickets should create the JSON file."""

        save_tickets(self.tickets, self.file_path)

        self.assertTrue(os.path.exists(self.file_path))

    def test_saved_data_matches_ticket_dictionary(self):
        """Saved JSON should preserve the ticket collection."""

        save_tickets(self.tickets, self.file_path)

        with open(self.file_path, "r", encoding="utf-8") as file:
            saved_tickets = json.load(file)

        self.assertEqual(saved_tickets, self.tickets)

    def test_save_empty_ticket_dictionary(self):
        """An empty collection should be saved successfully."""

        save_tickets({}, self.file_path)

        with open(self.file_path, "r", encoding="utf-8") as file:
            saved_tickets = json.load(file)

        self.assertEqual(saved_tickets, {})

    # ----------------------------------------
    # LOADING TESTS
    # ----------------------------------------

    def test_load_saved_tickets(self):
        """Saved tickets should load correctly."""

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(loaded_tickets, self.tickets)

    def test_load_empty_ticket_dictionary(self):
        """An empty JSON dictionary should load correctly."""

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({}, file)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(loaded_tickets, {})

    def test_loaded_tickets_preserve_notes(self):
        """Notes should remain available after saving and loading."""

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(
            loaded_tickets["T002"]["notes"],
            self.tickets["T002"]["notes"]
        )

    def test_loaded_tickets_preserve_assignment(self):
        """Assigned staff names should survive a reload."""

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(
            loaded_tickets["T002"]["assigned_to"],
            "John"
        )

    # ----------------------------------------
    # INVALID JSON TESTS
    # ----------------------------------------

    def test_corrupted_json_is_rejected(self):
        """Malformed JSON must not be accepted."""

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write('{"T001": ')

        with self.assertRaises((ValueError, OSError)):
            load_tickets(self.file_path)

    def test_duplicate_ticket_ids_are_rejected(self):
        """Two records with the same ID must not be accepted."""

        duplicate_tickets = [
            {
                "id": "T001",
                "title": "First ticket",
                "category": "Network",
                "urgency": "high",
                "affected_users": 10,
                "priority": "critical",
                "status": "open",
                "assigned_to": None,
                "notes": []
            },
            {
                "id": "T001",
                "title": "Second ticket",
                "category": "Hardware",
                "urgency": "low",
                "affected_users": 1,
                "priority": "low",
                "status": "open",
                "assigned_to": None,
                "notes": []
            }
        ]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(duplicate_tickets, file)

        with self.assertRaises((ValueError, TypeError, KeyError)):
            load_tickets(self.file_path)

    def test_invalid_ticket_record_is_rejected(self):
        """A ticket missing required fields must be rejected."""

        invalid_tickets = {
            "T001": {
                "id": "T001",
                "title": "Incomplete ticket"
            }
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(invalid_tickets, file)

        with self.assertRaises((ValueError, TypeError, KeyError)):
            load_tickets(self.file_path)

    # ----------------------------------------
    # IN-MEMORY SAFETY TESTS
    # ----------------------------------------

    def test_failed_load_does_not_change_existing_tickets(self):
        """
        If loading fails, an existing in-memory collection
        must remain unchanged.
        """

        current_tickets = deepcopy(self.tickets)
        original_tickets = deepcopy(current_tickets)

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.write("This is not valid JSON")

        with self.assertRaises((ValueError, OSError)):
            load_tickets(self.file_path)

        self.assertEqual(current_tickets, original_tickets)

    def test_failed_save_does_not_change_ticket_dictionary(self):
        """Saving should not unexpectedly modify ticket data."""

        original_tickets = deepcopy(self.tickets)

        invalid_path = os.path.join(
            self.temp_dir.name,
            "missing_directory",
            "tickets.json"
        )

        with self.assertRaises(OSError):
            save_tickets(self.tickets, invalid_path)

        self.assertEqual(self.tickets, original_tickets)


if __name__ == "__main__":
    unittest.main()