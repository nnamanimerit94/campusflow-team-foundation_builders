import unittest
import json
import os
import tempfile

from campusflow.storage import (
    create_storage,
    save_tickets,
    load_tickets
)


class TestStorage(unittest.TestCase):

    def setUp(self):
        # Create a temporary folder for testing
        self.temp_dir = tempfile.TemporaryDirectory()

        # Set the path for the test JSON file
        self.file_path = os.path.join(
            self.temp_dir.name,
            "tickets.json"
        )

        # Sample ticket data
        self.tickets = {
            "T001": {
                "id": "T001",
                "title": "Campus Wi-Fi is down",
                "category": "Network",
                "urgency": "high",
                "affected_users": 15,
                "priority": "critical",
                "status": "open",
                "assigned_to": None
            }
        }

    def tearDown(self):
        # Remove the temporary folder after each test
        self.temp_dir.cleanup()

    # Test 1: Create the JSON file
    def test_create_storage(self):
        create_storage(self.file_path)

        self.assertTrue(os.path.exists(self.file_path))

    # Test 2: New JSON file contains an empty dictionary
    def test_empty_storage(self):
        create_storage(self.file_path)

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.assertEqual(data, {})

    # Test 3: Save tickets to the JSON file
    def test_save_tickets(self):
        create_storage(self.file_path)

        save_tickets(self.tickets, self.file_path)

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.assertEqual(data, self.tickets)

    # Test 4: Load tickets from the JSON file
    def test_load_tickets(self):
        create_storage(self.file_path)

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(loaded_tickets, self.tickets)

    # Test 5: Load an empty ticket collection
    def test_load_empty_tickets(self):
        create_storage(self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(loaded_tickets, {})

    # Test 6: Saving tickets preserves their IDs
    def test_ticket_ids_are_preserved(self):
        create_storage(self.file_path)

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertIn("T001", loaded_tickets)

    # Test 7: Saving changes updates the JSON file
    def test_save_updated_ticket(self):
        create_storage(self.file_path)

        save_tickets(self.tickets, self.file_path)

        self.tickets["T001"]["status"] = "resolved"

        save_tickets(self.tickets, self.file_path)

        loaded_tickets = load_tickets(self.file_path)

        self.assertEqual(
            loaded_tickets["T001"]["status"],
            "resolved"
        )

    # Test 8: The JSON file contains valid JSON
    def test_valid_json(self):
        create_storage(self.file_path)

        save_tickets(self.tickets, self.file_path)

        with open(self.file_path, "r") as file:
            data = json.load(file)

        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()