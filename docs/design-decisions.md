# CampusFlow Next - Design Decisions

## 1. Purpose

This document explains the main technical decisions made while
improving the CampusFlow application.

The purpose is to make the code easier to understand, test,
maintain, and improve.

We will explain why we chose each approach and how we check
that it meets the assignment requirements.

We will build on the existing CampusFlow application rather
than starting again from scratch.

---

## 2. Technology Choices

### Decision

We will continue using Python and its standard library.

We will use:

- Python functions for organising the code.
- Dictionaries to store tickets.
- Lists to store follow-up notes.
- JSON files for persistent storage.
- unittest for automated testing.
- The command line for user interaction.

### Reason

These technologies are within the learning boundaries of the
assignment.

They allow us to improve the existing application without
introducing unnecessary complexity.

### Verification

We will check that the application runs using Python and that
the automated tests can be executed with:

`python -m unittest discover -s tests -v`

---

## 3. Ticket Data Structure

### Decision

Tickets will be stored in a dictionary of dictionaries.

Each ticket's unique ID will be the key of the outer dictionary.

Example:

    {
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
        }
    }

### Reason

Using the ticket ID as the key makes it straightforward to find
a ticket without searching through every ticket in the collection.

The inner dictionary stores the information belonging to that
ticket.

The notes field is a list because a ticket can have multiple
follow-up notes.

### Verification

We will test ticket creation and confirm that the ticket ID,
required fields, and notes list are stored correctly.

We will also test that ticket IDs remain unique.

---

## 4. Separation of Responsibilities

### Decision

We will keep different responsibilities in separate Python files.

The current project uses the following modules:

- `main.py`: starts the application and manages the menus.
- `campusflow/tickets.py`: handles ticket creation and related
  ticket operations.
- `campusflow/workflow.py`: handles assignment and status changes.
- `campusflow/storage.py`: handles JSON persistence.
- `campusflow/report.py`: calculates and displays reports.

Additional modules may be introduced for validation, notes,
search, or the understanding check if necessary.

### Reason

Separating responsibilities makes the code easier to understand.

For example, JSON loading and saving should not need to be
implemented separately inside every menu option.

It also makes individual functions easier to test.

### Verification

We will inspect the modules and run the tests for their
respective functions.

We will check that changes to one feature do not unintentionally
break other features.

---

## 5. Ticket Validation

### Decision

We will validate ticket information before creating or modifying
ticket records.

The required categories are:

- Network
- Hardware
- Software
- Other

The permitted urgency values are:

- low
- medium
- high

A title must not be blank after trimming whitespace.

The affected_users value must be a strictly positive integer.
Boolean values, floating-point values, and strings must be rejected.

### Reason

Invalid data can lead to incorrect priorities, unreliable reports,
and unexpected application behaviour.

Validating input before changing the ticket collection helps
prevent invalid operations from leaving partial changes behind.

### Verification

We will test valid and invalid ticket inputs.

We will include tests for zero, negative numbers, floats, and
boolean values for affected_users.

We will compare the ticket collection before and after rejected
operations to verify that it remains unchanged.

---

## 6. Priority Calculation

### Decision

We will preserve the original CampusFlow priority rules and
their required order.

The rules are:

1. Critical when urgency is high AND affected_users is at least 10.
2. Otherwise, high when urgency is high OR affected_users is
   at least 10.
3. Otherwise, medium when urgency is medium OR affected_users
   is at least 3.
4. Otherwise, low.

### Reason

The order matters because a ticket may satisfy more than one rule.

For example, a high-urgency ticket affecting 15 users must be
critical rather than merely high.

Preserving these rules ensures that the improved application
continues to behave as required by the original project.

### Verification

We will test examples for every priority level, including the
boundary values of 3 and 10 affected users.

---

## 7. Ticket Status Workflow

### Decision

We will preserve the required ticket lifecycle:

- open to in_progress
- in_progress to resolved
- resolved to open when reopened

An unassigned open ticket must not move to in_progress.

A resolved ticket must be reopened before it can return to
in_progress.

Assignment changes to resolved tickets must be rejected.

### Reason

The workflow represents the progress of a campus support request.

Allowing invalid transitions could make the ticket information
unreliable.

### Verification

We will test both permitted and prohibited transitions.

For rejected operations, we will verify that the ticket's data
remains unchanged.

---

## 8. Follow-up Notes

### Decision

Each ticket will contain a notes list.

Every note will contain:

- note_id
- author
- message

Note IDs will use the format N001, N002, N003, and so on,
within each ticket.

New notes will only be accepted for tickets with open or
in_progress status.

The author must not be blank.

The message must contain between 5 and 300 characters after
trimming whitespace.

### Reason

Structured notes allow support staff to record follow-up work
without changing the original ticket description.

Keeping notes inside their corresponding ticket makes it
straightforward to save and reload the complete ticket record.

### Verification

We will test valid notes, invalid authors, invalid messages,
and attempts to add notes to resolved tickets.

We will verify that rejected notes do not consume note IDs and
that existing notes survive saving, resolving, reopening, and
reloading tickets.

---

## 9. JSON Storage and Data Safety

### Decision

We will continue using JSON to save the ticket collection.

The application will create the JSON file if it does not exist.

When loading data, the application will validate the complete
collection before replacing the existing in-memory collection.

If loading fails, the existing collection must remain unchanged.

### Reason

JSON is suitable for this project because it provides a simple
way to save Python dictionary data between application runs.

Validating the complete collection before replacing the current
data prevents a partially loaded or invalid collection from
corrupting the application's state.

### Verification

We will test saving, loading, malformed JSON, invalid ticket
records, and ID continuity after reloading.

We will also verify that saved notes and assignments are preserved.

The supported JSON format will be documented in the README.

---

## 10. Ticket Search

### Decision

We will provide title searches using case-insensitive substring
matching.

Users will also be able to filter by category, status, and priority.

When multiple filters are supplied, a ticket must satisfy all
of them.

An empty filter will not restrict results for that field.

### Reason

Combined filters allow users to find relevant tickets more
quickly.

Using logical AND prevents tickets that match only one filter
from appearing in results that require several conditions.

Search will not modify the ticket collection.

### Verification

We will test case-insensitive title searches, combined filters,
empty filters, and invalid filter values.

We will also compare the ticket collection before and after
searching to confirm that no ticket data was changed.

---

## 11. Reports and Analytics

### Decision

The reports will include:

- Total tickets.
- Counts by status.
- Counts by priority.
- Counts by category.
- Unresolved ticket count.
- Resolved ticket count.
- Resolution percentage.

Unresolved tickets are those currently in open or in_progress
status.

Resolution percentage will be calculated as:

    resolved tickets / total tickets * 100

When there are no tickets, the resolution percentage will be 0%.

### Reason

These statistics provide a clearer view of the campus helpdesk's
current workload and resolution progress.

Counting tickets according to their current status avoids
double-counting tickets that have been reopened.

### Verification

We will test reports using known ticket collections, including
empty collections, all-resolved collections, and reopened tickets.

We will compare the calculated totals and percentages with
manually calculated expected results.

---

## 12. Open Work Queue

### Decision

The original Open Work Queue will continue to display only
tickets whose status is open.

Tickets will be ordered by priority:

1. Critical
2. High
3. Medium
4. Low

Tickets with the same priority will be ordered by their numeric
ticket ID, with earlier IDs first.

Tickets with in_progress or resolved status will not appear
in this queue.

### Reason

The queue is intended to show tickets that are open and awaiting
work.

Keeping this queue separate from general search results preserves
the original application's behaviour.

### Verification

We will test the queue with tickets having different priorities,
different statuses, and IDs such as T002 and T010.

We will verify that only open tickets appear and that the ordering
is correct.

---

## 13. Automated Testing

### Decision

We will use Python's built-in unittest framework.

Tests will cover normal operations, invalid inputs, boundary
conditions, and data preservation after rejected operations.

### Reason

Manual testing alone does not provide a repeatable way to verify
that the application continues to work after changes.

Automated tests allow us to run the same checks whenever the
code changes.

### Verification

We will run the test suite using:

`python -m unittest discover -s tests -v`

The assignment requires at least 14 meaningful automated tests
across the integrated application.

At least five tests must be authored by each engineer.

We will record actual test results and investigate failures
before declaring the application complete.

---

## 14. GitHub Collaboration and Code Review

### Decision

We will use separate feature branches and pull requests for
our work.

Each engineer will contribute code and tests and review the
other engineer's changes.

### Reason

Working through branches and pull requests allows changes to
be reviewed before they are merged into the main branch.

Specific review comments help identify missing tests, incorrect
assumptions, and potential problems.

### Verification

We will retain evidence of:

- Feature branches and commits.
- Pull requests authored by each engineer.
- Specific peer review comments.
- Changes made in response to feedback.
- Test results after integration.

---

## 15. Use of AI

### Decision

We will use AI to help explain concepts, suggest experiments,
and identify possible edge cases.

We will not assume that AI-generated code or advice is correct
without checking it.

### Reason

AI can support learning, but it may suggest code that does not
match our existing project or the assignment requirements.

Independent verification helps us understand the final
implementation rather than simply copying a solution.

### Verification

We will document our learning cycles in `docs/ai-learning-log.md`.

We will record the questions asked, experiments performed,
evidence collected, and final decisions.

Both engineers must be able to explain their own contributions
during the project demonstration.

---

## 16. Summary

Our design decisions aim to preserve the original CampusFlow
features while improving reliability, validation, storage,
search, reporting, testing, and maintainability.

We will evaluate these decisions against the assignment
requirements and actual test results.

Any decision that changes during implementation will be
updated in this document with an explanation of the reason
for the change.