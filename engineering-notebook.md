# Engineering Notebook

## Day 1

### Lessons

- Constructors should avoid side effects.
- Separate business logic from user interaction.
- Type hints improve readability.
- Comments should explain why, not what.
- Good commit messages tell a story.
- Pull requests should contain small, focused changes.

### Questions

- When should I use properties?
- When should I introduce logging?

### New Concepts

- Separation of concerns
- Type hints
- Pull Request workflow


# Engineering Notebook

## Day 1

### Topics

- Module organization
- Docstrings
- Type hints
- Separation of concerns

### Key Lessons

- Classes should model data rather than perform user interaction.
- Validation should be reusable.
- Keep commits focused on a single concern.

---

## Day 2

### Topics

- Logging
- Validation
- Business rules
- Professional code reviews

### Lessons Learned

- Logging should be configured once.
- Use `logging.getLogger(__name__)` in each module.
- `basicConfig()` only runs once unless `force=True` is used.
- Validation functions should have a single responsibility.
- Business validation is different from type validation.
- Avoid relying on truthiness (`if not value`) when `None` is the actual invalid state.

### New Concepts

- Logging levels
- File handlers
- Module loggers
- Separation of concerns