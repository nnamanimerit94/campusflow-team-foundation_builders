import unittest

from campusflow.report import generate_report


class TestCampusFlowReports(unittest.TestCase):

    def setUp(self):
        """Create sample tickets for testing reports."""

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
                "notes": []
            },
            "T003": {
                "id": "T003",
                "title": "Software installation failed",
                "category": "Software",
                "urgency": "low",
                "affected_users": 1,
                "priority": "low",
                "status": "resolved",
                "assigned_to": "Mary",
                "notes": []
            },
            "T004": {
                "id": "T004",
                "title": "Printer is not working",
                "category": "Hardware",
                "urgency": "high",
                "affected_users": 2,
                "priority": "high",
                "status": "resolved",
                "assigned_to": "John",
                "notes": []
            }
        }

    def test_total_ticket_count(self):
        """The report should count all tickets."""

        report = generate_report(self.tickets)

        self.assertEqual(report["total_tickets"], 4)

    def test_status_counts(self):
        """The report should count tickets by status."""

        report = generate_report(self.tickets)

        self.assertEqual(report["status_counts"]["open"], 1)
        self.assertEqual(report["status_counts"]["in_progress"], 1)
        self.assertEqual(report["status_counts"]["resolved"], 2)

    def test_priority_counts(self):
        """The report should count tickets by priority."""

        report = generate_report(self.tickets)

        self.assertEqual(report["priority_counts"]["critical"], 1)
        self.assertEqual(report["priority_counts"]["high"], 1)
        self.assertEqual(report["priority_counts"]["medium"], 1)
        self.assertEqual(report["priority_counts"]["low"], 1)

    def test_category_counts(self):
        """The report should count tickets by category."""

        report = generate_report(self.tickets)

        self.assertEqual(report["category_counts"]["Network"], 1)
        self.assertEqual(report["category_counts"]["Hardware"], 2)
        self.assertEqual(report["category_counts"]["Software"], 1)
        self.assertEqual(report["category_counts"]["Other"], 0)

    def test_unresolved_ticket_count(self):
        """Open and in-progress tickets are unresolved."""

        report = generate_report(self.tickets)

        self.assertEqual(report["unresolved_count"], 2)

    def test_resolved_ticket_count(self):
        """The report should count resolved tickets."""

        report = generate_report(self.tickets)

        self.assertEqual(report["resolved_count"], 2)

    def test_resolution_percentage(self):
        """Resolution percentage should be calculated correctly."""

        report = generate_report(self.tickets)

        self.assertEqual(report["resolution_percentage"], 50.0)

    def test_empty_ticket_collection(self):
        """An empty collection should produce zero counts and 0%."""

        report = generate_report({})

        self.assertEqual(report["total_tickets"], 0)
        self.assertEqual(report["unresolved_count"], 0)
        self.assertEqual(report["resolved_count"], 0)
        self.assertEqual(report["resolution_percentage"], 0.0)

    def test_all_tickets_resolved(self):
        """The resolution percentage should be 100% when all
        tickets are resolved.
        """

        resolved_tickets = {
            "T001": {
                **self.tickets["T001"],
                "status": "resolved"
            },
            "T002": {
                **self.tickets["T002"],
                "status": "resolved"
            }
        }

        report = generate_report(resolved_tickets)

        self.assertEqual(report["resolved_count"], 2)
        self.assertEqual(report["unresolved_count"], 0)
        self.assertEqual(report["resolution_percentage"], 100.0)

    def test_reopened_ticket_counts_as_open(self):
        """A reopened ticket should count according to its current status."""

        reopened_tickets = {
            "T001": {
                **self.tickets["T001"],
                "status": "open"
            },
            "T002": {
                **self.tickets["T002"],
                "status": "resolved"
            }
        }

        report = generate_report(reopened_tickets)

        self.assertEqual(report["status_counts"]["open"], 1)
        self.assertEqual(report["status_counts"]["resolved"], 1)
        self.assertEqual(report["unresolved_count"], 1)
        self.assertEqual(report["resolved_count"], 1)
        self.assertEqual(report["resolution_percentage"], 50.0)

    def test_status_counts_add_up_to_total(self):
        """Every ticket should be counted in exactly one status."""

        report = generate_report(self.tickets)

        total_by_status = sum(report["status_counts"].values())

        self.assertEqual(total_by_status, report["total_tickets"])

    def test_priority_counts_add_up_to_total(self):
        """Every ticket should be counted in exactly one priority."""

        report = generate_report(self.tickets)

        total_by_priority = sum(report["priority_counts"].values())

        self.assertEqual(total_by_priority, report["total_tickets"])

    def test_report_does_not_modify_tickets(self):
        """Generating reports should not change the ticket collection."""

        import copy

        original_tickets = copy.deepcopy(self.tickets)

        generate_report(self.tickets)

        self.assertEqual(self.tickets, original_tickets)


if __name__ == "__main__":
    unittest.main()