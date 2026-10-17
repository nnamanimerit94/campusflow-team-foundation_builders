# CampusFlow Baseline Check

## 1. Purpose

This document records the initial condition of the CampusFlow
application before implementing the CampusFlow Next improvements.

The purpose is to check the existing application, identify problems,
and establish a baseline against which we can compare our improvements.

## 2. Application Run

Command used:

`python main.py`

Result:

[Write whether the application started successfully.
If an error occurred, describe the error.]

Observations:

- The application displays the CampusFlow welcome message.
- The application asks the user to choose between Admin and Student.
- The application displays the appropriate menu after a selection.

[Keep only the observations you actually verified.]

## 3. Existing Automated Tests

Command used:

`python -m unittest discover -s tests -v`

Result:

- Total tests run: [Enter number]
- Tests passed: [Enter number]
- Tests failed: [Enter number]
- Errors: [Enter number]

Observations:

[Describe any test failures, errors, or problems encountered.
If all tests passed, state that and record the evidence.]

## 4. Manual Testing

### Test 1: Ticket Creation

Input:

[Describe the input used to create a ticket.]

Expected result:

The application should create a ticket with the correct details
and calculate its priority according to the original priority rules.

Actual result:

[Describe what actually happened.]

Status: [Pass/Fail]

### Test 2: Ticket Assignment and Status Update

Input:

[Describe the ticket ID, staff name, and status option entered.]

Expected result:

The application should assign the ticket and update its status
according to the supported workflow.

Actual result:

[Describe what actually happened.]

Status: [Pass/Fail]

### Test 3: JSON Persistence

Input:

Create or update a ticket, close the application, and reopen it.

Expected result:

The ticket should be saved in the JSON file and remain available
after restarting the application.

Actual result:

[Describe what actually happened.]

Status: [Pass/Fail]

## 5. Audit Findings

The CampusFlow audit identified areas that require further
investigation and improvement.

The CampusFlow Next assignment focuses on the following areas:

1. Stronger validation of ticket data and operations.
2. Safe ticket status transitions and assignment rules.
3. Structured follow-up notes for tickets.
4. Search using multiple filters.
5. More complete and reliable reports.
6. Safe JSON loading, validation, and saving.
7. Automated tests for normal and invalid operations.
8. Clear documentation and meaningful peer review.

These are the improvement areas specified in the assignment.
They are not necessarily confirmed defects in the original application.

## 6. Baseline Conclusion

The initial checks establish the starting condition of CampusFlow
before the CampusFlow Next improvements.

The application and its tests were examined to identify existing
behaviour and areas requiring further investigation.

The results recorded above will be used to compare the original
application with the improved version.

## 7. Next Steps

Based on the actual test results and investigation, the next steps are:

1. Review ticket validation and priority calculation.
2. Verify that invalid operations leave ticket data unchanged.
3. Improve JSON validation and persistence where necessary.
4. Implement structured follow-up notes.
5. Implement combined ticket search and improved reports.
6. Add automated tests for the required behaviours.
7. Document the changes and verify them through peer review.