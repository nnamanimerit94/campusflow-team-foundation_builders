# AI Learning Log — CampusFlow

## 1. Introduction

During the development of CampusFlow, we used ChatGPT as an AI
assistant to help us understand Python programming concepts,
organize our code, and develop the application's features.

We did not rely on AI alone. We reviewed the suggested code and
worked to understand how the different functions operate.

## 2. AI Tool Used

- Tool: ChatGPT
- Purpose: Learning Python, debugging, generating code suggestions,
  writing tests, and improving project organization.

## 3. Learning Activities

### Activity 1: Creating the Main Menu

**Task:**
Create a main menu that allows users to select Admin, Student, or Exit.

**How AI helped:**
ChatGPT suggested using a function, a while loop, and if-elif
statements to display the menu and process the user's selection.

**What I learned:**
- How to define a function using `def`.
- How to use `while True` to repeat a menu.
- How to collect user input with `input()`.
- How to use `if`, `elif`, and `else`.
- How to use `break` to exit a loop.

**My contribution:**
I modified the suggested code to create separate menus for
administrators and students.

**Verification:**
I ran the program and checked whether the correct menu appeared
for each selection.

### Activity 2: Loading Tickets from JSON

**Task:**
Load ticket information from a JSON file into Python.

**How AI helped:**
ChatGPT explained how to use Python's `json` and `os` modules
to create a JSON file if it does not exist and load its contents.

**What I learned:**
- How to open files using `open()`.
- How to use `os.path.exists()` to check whether a file exists.
- How to use `json.load()` to read JSON data.
- How JSON objects can be represented as Python dictionaries.
- Why JSON uses `null` instead of Python's `None`.

**My contribution:**
I decided to store tickets in a dictionary of dictionaries,
using each ticket ID as the key.

**Verification:**
I checked that the JSON structure matched the dictionary structure
required by the application.

### Activity 3: Creating Ticket Functions

**Task:**
Implement functions for creating, viewing, and assigning tickets.

**How AI helped:**
ChatGPT suggested functions that accept the ticket dictionary
as an argument and perform operations on it.

**What I learned:**
- How to define functions with parameters.
- How to access dictionary values using keys.
- How to add new entries to a dictionary.
- How to update ticket information.
- How to validate user input.

**My contribution:**
I integrated the functions into the menus in `main.py` and
organized the ticket-related functions in `tickets.py`.

**Verification:**
I checked the ticket dictionary after creating or assigning
a ticket to confirm that the expected values had changed.

### Activity 4: Updating Ticket Status and Work Queue

**Task:**
Allow administrators to update ticket status and view the work queue.

**How AI helped:**
ChatGPT suggested using conditional statements to update ticket
statuses and sorting tickets according to priority.

**What I learned:**
- How to update dictionary values.
- How to use conditions to validate menu choices.
- How to filter tickets based on their status.
- How to sort tickets using a priority order.

**My contribution:**
I connected the functions to the appropriate options in the
Admin menu.

**Verification:**
I checked whether tickets had the expected status and whether
the work queue displayed unresolved tickets in priority order.

### Activity 5: Writing Automated Tests

**Task:**
Write automated tests for ticket and workflow functions.

**How AI helped:**
ChatGPT introduced me to Python's `unittest` module and showed
how to test functions using sample ticket dictionaries.

**What I learned:**
- How to create a test class.
- How to use `setUp()` to prepare test data.
- How to use assertions such as `assertEqual()` and `assertIn()`.
- How to simulate user input using `unittest.mock.patch`.
- Why automated tests help detect errors.

**My contribution:**
I organized the suggested tests into separate files for ticket
operations, workflow operations, and storage operations.

**Verification:**
I planned to run the tests using Python's unittest test discovery
and investigate any failures.

## 4. Critical Evaluation of AI Suggestions

AI-generated code must be reviewed before being accepted.

During development, I learned that:

- Suggested code may not match the existing project structure.
- Function names and parameters must match across files.
- Updating a dictionary in memory does not automatically save
  changes to a JSON file.
- JSON uses `null`, whereas Python uses `None`.
- Tests must match the actual implementation.
- A program should be tested rather than assumed to work because
  an AI assistant generated the code.

I used these lessons to review the suggested code and consider
how the different modules should work together.

## 5. Improvements and Future Learning

The next areas I intend to improve are:

- Implementing reliable JSON saving and loading.
- Testing the complete application.
- Handling invalid input consistently.
- Improving ticket ID generation.
- Understanding the code well enough to explain it independently.
- Reviewing code changes with my teammate.

## 6. Conclusion

Using ChatGPT helped me explore Python programming and understand
how to divide an application into smaller functions and modules.

The process also taught me that AI-generated code requires
human review, testing, and verification before it can be trusted.