# CampusFlow Next - AI Learning Log

## 1. Purpose

This document records how we used AI to understand programming
concepts and improve our CampusFlow application.

We used AI to explain concepts, suggest test cases, compare possible
solutions, and help us understand problems.

We did not treat AI-generated code or advice as automatically correct.
We checked suggestions against our requirements, experiments, and
automated tests.

Our aim was to understand the code we implemented and be able to
explain our decisions without AI assistance.

---

# ENGINEER A - Ticket Safety and Storage Engineer

## Learning Cycle A1: Validating Data Before Changing It

### 1. Original concept gap

I initially needed a better understanding of how to validate ticket
information before changing the ticket collection.

I also needed to understand why an invalid operation must not leave
partially modified data behind.

### 2. Exact question asked AI

"Explain how to validate a dictionary before mutating it, using a
book library example, then quiz me."

### 3. Summary of AI guidance

AI explained that a program should check whether the supplied data
meets the requirements before changing the original collection.

For example, before assigning a ticket to a staff member, the
program should check that the ticket exists, the staff name is not
blank, and the ticket is not resolved.

If validation fails, the program should reject the operation without
changing the ticket.

This approach helps keep the application's data consistent.

### 4. Small unrelated experiment

I used a small dictionary representing books in a library.

I attempted to change a book's availability only after checking
whether the book existed.

I also tested an invalid book ID to observe whether the original
dictionary remained unchanged.

Experiment code:

[Insert the small experiment you actually performed.]

### 5. Independent verification

I checked the behaviour by comparing the dictionary before and
after an invalid operation.

I also examined the relevant CampusFlow requirements and wrote
tests for invalid ticket operations.

Evidence:

[Record the test name and actual result.]

### 6. Final engineering decision

I decided to validate input before modifying ticket data.

I will use automated tests to check that rejected operations leave
the ticket collection unchanged.

### 7. Personal reflection

Before this exercise, I thought checking whether an operation was
valid was enough.

I learned that I must also check whether the operation changed any
data before it was rejected.

I can demonstrate this by comparing the ticket collection before
and after an invalid operation.

---

## Learning Cycle A2: Safe JSON Loading

### 1. Original concept gap

I needed to understand why successfully reading a JSON file does
not guarantee that its contents are valid for CampusFlow.

A file can contain valid JSON but still contain incomplete or
inconsistent ticket records.

### 2. Exact question asked AI

"Why might json.load succeed but return unsafe or inconsistent
business data?"

### 3. Summary of AI guidance

AI explained that JSON decoding checks whether the file contains
valid JSON syntax. It does not automatically verify all the rules
required by an application.

For example, a ticket could have a valid JSON structure but contain
an invalid category, an unsupported status, or a missing notes field.

The application therefore needs to validate the decoded data
before accepting it as its ticket collection.

### 4. Small unrelated experiment

I created a small JSON file representing a book collection.

The JSON syntax was valid, but one book record was missing a
required field.

I checked whether the file could be decoded and whether my own
validation logic detected the missing field.

Experiment code:

[Insert the small experiment you actually performed.]

### 5. Independent verification

I compared the results of JSON decoding with the results of
application-level validation.

I also tested how CampusFlow responds to invalid stored data.

Evidence:

[Record the test name and actual result.]

### 6. Final engineering decision

I decided that CampusFlow must validate the complete ticket
collection before replacing the current in-memory data.

If loading fails, the existing ticket collection must remain
unchanged.

I will verify this behaviour using automated tests.

### 7. Personal reflection

I learned that valid JSON is not necessarily valid application data.

I now understand why decoding and validation are separate steps.

I will use this distinction when implementing and reviewing
CampusFlow's storage functions.

---

# ENGINEER B - Search, Reporting and CLI Engineer

## Learning Cycle B1: Combining Search Filters

### 1. Original concept gap

I needed to understand how multiple search filters should work
together.

For example, a user might search for a title containing "wifi"
while also selecting the Network category and open status.

### 2. Exact question asked AI

"Compare casefold and lower for search; suggest test cases but do
not implement my project."

### 3. Summary of AI guidance

AI explained that case-insensitive substring matching can be
implemented by converting the title and search text to a consistent
case before checking whether one contains the other.

The search filters must use logical AND.

This means a ticket must satisfy every supplied filter to appear
in the results.

An empty filter means that the corresponding field should not
restrict the results.

### 4. Small unrelated experiment

I created a small list of book titles and searched them using
different letter cases.

I then combined a title search with a category filter to check
whether only matching books were returned.

Experiment code:

[Insert the small experiment you actually performed.]

### 5. Independent verification

I compared the experiment's results with the expected results.

I also created or reviewed tests for case-insensitive title matching
and combined filters.

Evidence:

[Record the test name and actual result.]

### 6. Final engineering decision

I decided that CampusFlow search should use case-insensitive
substring matching and apply all supplied filters together.

I will keep search read-only so that searching cannot accidentally
change ticket data.

### 7. Personal reflection

I learned that using several filters is different from returning
records that match any one of them.

I can explain the use of logical AND by showing a test where a
ticket matches the title but fails the category filter.

---

## Learning Cycle B2: Reliable Report Calculations

### 1. Original concept gap

I needed to understand how to calculate ticket statistics without
counting tickets incorrectly.

I also needed to understand what should happen when the ticket
collection is empty.

### 2. Exact question asked AI

"Explain how to calculate counts and percentages from a dictionary
of records, including how to handle an empty collection."

### 3. Summary of AI guidance

AI explained that each ticket should be counted according to its
current status.

The unresolved count is the sum of open and in-progress tickets.

The resolved count includes only tickets whose current status is
resolved.

The resolution percentage is calculated as:

Resolution percentage = resolved tickets / total tickets * 100

An empty collection needs special handling because division by
zero is not allowed.

For an empty collection, the required resolution percentage is 0%.

### 4. Small unrelated experiment

I created a small dictionary of library books with different
availability states.

I counted the books in each state and calculated the percentage
that were available.

I also tested the calculation when the dictionary was empty.

Experiment code:

[Insert the small experiment you actually performed.]

### 5. Independent verification

I calculated the expected results manually and compared them
with the results from my experiment.

I also checked the report tests for empty collections and
known ticket fixtures.

Evidence:

[Record the test name and actual result.]

### 6. Final engineering decision

I decided to calculate report statistics from the tickets'
current data.

I will handle an empty collection explicitly and test the report
using both empty and non-empty datasets.

### 7. Personal reflection

I learned that a report should be checked against known expected
results rather than judged only by whether it displays numbers.

I can verify the calculations using a small ticket collection
whose status counts and resolution percentage I know in advance.

---

# TEAM LEARNING CYCLE: Reviewing an AI Suggestion

## 1. Original concept gap

We needed to understand how to determine whether an AI-generated
suggestion was appropriate for our existing CampusFlow project.

### 2. Exact question asked AI

[Insert a real question asked by one of the engineers.]

### 3. AI suggestion

[Describe the actual suggestion made by AI.]

### 4. Independent verification

We compared the suggestion with the assignment requirements,
the existing project structure, and relevant test results.

Evidence:

[Describe the experiment, documentation, or test used.]

### 5. Final decision

[Explain whether we accepted, changed, or rejected the suggestion
and give the reason supported by our evidence.]

### 6. What we learned

We learned that an AI suggestion must be checked against the
actual application requirements and implementation.

A suggestion that appears reasonable may still be unsuitable
for our existing project.

We should be able to explain our final decision using evidence.