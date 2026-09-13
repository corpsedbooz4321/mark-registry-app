# mark-registry-app

## What is the project?

Mark Registry App is a lightweight Python command-line application for managing student marks from the terminal. It is designed for small coaching setups, tutoring environments, or learning projects that need a simple registry without the overhead of a full web app.

The current version supports checking student results, updating marks, removing entries, viewing all saved data, and persisting records in a JSON file.

## Features

- Menu-driven CLI for checking, updating, removing, and viewing records
- Input validation for student names and mark values
- Case-insensitive lookup and update flow
- JSON-based persistence for saved records
- Average calculation for student results
- Colored terminal output and simple on-screen formatting

## Installation

Requirements:

- Python 3.8 or newer

From the repository root, run:

```bash
python3 Mark-Registry-app/main.py
```

If you prefer to work from inside the app folder, run:

```bash
cd Mark-Registry-app
python3 main.py
```

No extra packages are required for the current version.

## Usage

When the app starts, you will see a menu with options such as:

- A: View all saved student data
- C: Check a student's result
- D: Remove an entry
- U: Update or add marks
- H: Show help
- Q: Exit the application

Data is stored in:

```text
Mark-Registry-app/database/data.json
```

Use the menu prompts to add or update marks, then save changes when prompted.
