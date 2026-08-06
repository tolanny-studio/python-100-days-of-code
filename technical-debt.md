# Technical Debt

## Day 1

### Logging

Not implemented.

Reason:
Small console application.

Future:
Introduce Python's logging module.

---

### Unit Tests

Not implemented.

Reason:
Testing has not yet been introduced.

Future:
Use pytest.

---

### Configuration

Prompt strings remain in main.py.

Reason:
Acceptable for project size.

Future:
Move to a configuration module if the project grows.


# Technical Debt

This document tracks improvements intentionally postponed for future learning.

## Day 2

### Decimal Instead of Float

Financial calculations should eventually use Python's `decimal.Decimal` module to avoid floating-point precision issues.

Status:
- Deferred

---

### Unit Testing

Validation functions should be covered with automated tests.

Status:
- Deferred

---

### Custom Exceptions

Introduce custom exception types for validation failures.

Status:
- Deferred

---

### Configuration

Move prompts and application settings into a dedicated configuration module.

Status:
- Deferred