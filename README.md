# mark-registry-app

A lightweight Python CLI application for tracking student marks. The project currently focuses on checking and updating results through a simple terminal menu.

## Current implementation

The app is organized into a small modular structure under the main directory:

- main/main.py: CLI entry point and menu loop.
- main/check.py: handles result lookup by student name.
- main/update.py: handles adding or updating a student's marks.
- main/data.py: stores the current in-memory registry data.

## Features

- Menu-driven CLI with options to check results, update results, or exit.
- Name validation to prevent numeric input.
- Case-insensitive lookup and update flow.
- Small modular file layout to separate responsibilities.

## How to run

From the repository root:

```bash
python3 main/main.py
```

Or from the main directory:

```bash
cd main
python3 main.py
```

## Project status

The application is still in its early CLI stage. The next major milestone is replacing the in-memory registry with persistent storage such as JSON or SQLite.
