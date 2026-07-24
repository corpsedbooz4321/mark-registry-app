# mark-registry-app

A lightweight Python CLI application for tracking student marks. The project currently focuses on checking and updating results through a simple terminal menu.

## What the app does

The current version lets you:

- view a student's marks by entering their name
- add or update marks for a student and subject
- keep entering records during the same session without returning to the main menu
- validate names and marks to reduce invalid input

## Project structure

The app is organized into a small modular layout under the main directory:

- main/main.py: CLI entry point and menu loop
- main/check.py: result lookup by student name
- main/update.py: add or update marks for a student
- main/data.py: sample in-memory registry data
- main/data.json: example JSON data for reference

## Features

- menu-driven CLI with options to check results, update results, or exit
- name validation to prevent numeric input
- case-insensitive lookup and update flow
- simple modular structure for easier maintenance

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

## Current status

The app is still in an early CLI stage. It uses an in-memory registry defined in main/data.py, and the JSON file is included as an example dataset rather than a fully connected persistence layer yet.

## Planned next steps

- connect the app to persistent storage such as JSON or SQLite
- add better formatting and search options
- expand the registry with more student details and reporting features
