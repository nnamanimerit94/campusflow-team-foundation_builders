# CampusFlow — Design Decisions

## 1. Introduction

CampusFlow is a Python command-line application designed to manage
technical support requests on campus.

The application allows students to create and view support tickets.
Administrators can view tickets, assign tickets to staff members,
update ticket statuses, view the work queue, and generate reports.

This document explains the main design decisions made during
the development of CampusFlow.

## 2. Programming Language

**Decision:** Use Python.

**Reason:**

Python was selected because it has simple and readable syntax.
It is suitable for beginners and allows us to build a command-line
application without requiring a complicated user interface.

Python also provides built-in modules for working with JSON,
handling files, and writing automated tests.

## 3. Command-Line Interface

**Decision:** Use a command-line interface.

**Reason:**

A command-line interface is simple to implement and allows users
to interact with the application through menus.

When the application starts, the user chooses between Admin,
Student, or Exit.

The selected role determines which menu is displayed.

This approach allows us to focus on the ticket management
features before developing a graphical user interface.

## 4. Separate Admin and Student Menus

**Decision:** Provide different menus for administrators and students.

**Reason:**

Students and administrators have different responsibilities.

Students can create and view support tickets, while administrators
can manage tickets, assign them to staff, update their status,
view the work queue, and generate reports.

Separate menus make the application easier to understand
and organize.

**Limitation:**

Selecting Admin or Student currently determines which menu is
displayed. It does not authenticate the user or enforce security
permissions.

Authentication and proper access control would be needed if the
application were used in a real campus environment.

## 5. Ticket Data Structure

**Decision:** Store tickets in a dictionary of dictionaries.

**Reason:**

Each ticket has a unique ID, such as T001 or T002.

The ticket ID is used as the key in the main dictionary, while
the ticket details are stored in an inner dictionary.

For example:

```python
tickets = {
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