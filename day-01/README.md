# Day 1 – Band Name Generator

## Overview

A simple command-line application that generates a band name using the user's city name and pet name.

This project is part of my **100 Days of Python** journey, but it has also been professionally refactored to follow software engineering best practices.

## Features

- Input validation
- Input sanitization
- Type hints
- Separation of concerns
- Colored terminal output
- Clean project structure

## Project Structure

```
day-01/
├── bandname.py
├── main.py
├── validateinput.py
└── README.md
```

## How to Run

```bash
python main.py
```

## Sample Output

```
Welcome to the Band Name Generator.

What is your city name?
> Lagos

What is your pet name?
> Lucky

The name of your band is Lagos Lucky
```

## Lessons Learned

- Writing clean functions
- Separating business logic from input handling
- Using type hints
- Writing meaningful commit messages
- Working with Git branches and pull requests

## Future Improvements

- Logging
- Unit tests
- Configuration module