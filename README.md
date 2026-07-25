# mark-registry-app

A lightweight Python CLI application for tracking student marks using a JSON-backed registry. The project currently focuses on checking and updating results through a simple terminal menu.

## What the app does

The current version lets you:

- view a student's marks by entering their name
- add or update marks for a student and subject
- save updates to `main/data.json`
- validate names and marks to reduce invalid input

## Project structure

The app is organized into a small modular layout under the main directory:

- main/main.py: CLI entry point and menu loop
- main/check.py: result lookup by student name
- main/update.py: add or update marks for a student
- main/data.json: JSON-backed student registry

## Features

- menu-driven CLI with options to check results, update results, or exit
- name validation to prevent numeric input
- case-insensitive lookup and update flow
- JSON persistence for saved student records
- ability to add multiple subjects before saving changes

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

The app currently uses `main/data.json` as the registry data store. New and updated marks are written back to the JSON file when the user finishes entering subject scores.

## Planned next steps

- improve persistent storage with optional SQLite or CSV support
- add better formatting and search options
- expand the registry with more student details and reporting features
- add a clearer save/feedback workflow in the CLI

## Update Log

- Latest update: July 25, 2026
