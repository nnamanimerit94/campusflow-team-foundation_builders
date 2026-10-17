import unittest

from campusflow.tickets import create_ticket


class TestTicketCreation(unittest.TestCase):

    def test_create_valid_ticket(self):
        """Test that a ticket can be created with valid information."""

        ticket = create_ticket(
            title="Campus Wi-Fi is down",
            category="Network",
            urgency="high",
            affected_users=15
        )

        self.assertEqual(ticket["title"], "Campus Wi-Fi is down")
        self.assertEqual(ticket["category"], "Network")
        self.assertEqual(ticket["urgency"], "high")
        self.assertEqual(ticket["affected_users"], 15)
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])
        self.assertEqual(ticket["notes"], [])

    def test_high_urgency_and_many_users_is_critical(self):
        """High urgency and at least 10 affected users means critical."""

        ticket = create_ticket(
            title="Network outage",
            category="Network",
            urgency="high",
            affected_users=10
        )

        self.assertEqual(ticket["priority"], "critical")

    def test_high_urgency_alone_is_high(self):
        """High urgency with fewer than 10 users means high priority."""

        ticket = create_ticket(
            title="Software problem",
            category="Software",
            urgency="high",
            affected_users=2
        )

        self.assertEqual(ticket["priority"], "high")

    def test_many_users_alone_is_high(self):
        """At least 10 affected users means high priority
        when urgency is not high.
        """

        ticket = create_ticket(
            title="Hardware problem",
            category="Hardware",
            urgency="low",
            affected_users=10
        )

        self.assertEqual(ticket["priority"], "high")

    def test_medium_urgency_gives_medium_priority(self):
        """Medium urgency with fewer than 3 users means medium."""

        ticket = create_ticket(
            title="Application issue",
            category="Software",
            urgency="medium",
            affected_users=1
        )

        self.assertEqual(ticket["priority"], "medium")

    def test_three_affected_users_gives_medium_priority(self):
        """At least 3 affected users means medium priority
        when the higher-priority rules do not apply.
        """

        ticket = create_ticket(
            title="Computer issue",
            category="Hardware",
            urgency="low",
            affected_users=3
        )

        self.assertEqual(ticket["priority"], "medium")

    def test_low_priority_ticket(self):
        """Low urgency and fewer than 3 users means low priority."""

        ticket = create_ticket(
            title="Minor issue",
            category="Other",
            urgency="low",
            affected_users=1
        )

        self.assertEqual(ticket["priority"], "low")

    def test_blank_title_is_rejected(self):
        """A title containing only whitespace must be rejected."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="   ",
                category="Network",
                urgency="high",
                affected_users=5
            )

    def test_invalid_category_is_rejected(self):
        """Only the four permitted categories should be accepted."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Electricity",
                urgency="high",
                affected_users=5
            )

    def test_invalid_urgency_is_rejected(self):
        """Urgency must be low, medium or high."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Network",
                urgency="urgent",
                affected_users=5
            )

    def test_zero_affected_users_is_rejected(self):
        """Affected users must be greater than zero."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Network",
                urgency="high",
                affected_users=0
            )

    def test_negative_affected_users_is_rejected(self):
        """Negative affected-user counts must be rejected."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Network",
                urgency="high",
                affected_users=-5
            )

    def test_float_affected_users_is_rejected(self):
        """Affected users must be an integer, not a float."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Network",
                urgency="high",
                affected_users=2.5
            )

    def test_boolean_affected_users_is_rejected(self):
        """Boolean values must not be accepted as integers."""

        with self.assertRaises((ValueError, TypeError)):
            create_ticket(
                title="Network problem",
                category="Network",
                urgency="high",
                affected_users=True
            )


if __name__ == "__main__":
    unittest.main()