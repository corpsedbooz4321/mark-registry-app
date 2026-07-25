# mark-registry-app

A lightweight Python CLI application for managing a simple student marks registry from the terminal. The project currently focuses on checking existing results and adding or updating marks for students through a menu-driven interface.

## What the app does

The current version lets you:

- look up a student's marks by entering their name
- add or update subject marks for a student
- save changes to the JSON registry file
- validate names and marks to reduce invalid input
- enter multiple subjects in one update session before saving

## Project structure

The app is organized into a small modular layout under the main directory:

- main/main.py: CLI entry point and menu loop
- main/check.py: result lookup and display for a student
- main/update.py: add or update marks and persist them to the registry
- main/banner.py: ASCII banners and terminal separators
- main/colors.py: color constants for terminal output
- main/data.json: example JSON-backed student registry

## Features

- menu-driven CLI with options to check results, update results, or exit
- input validation for student names and marks
- case-insensitive lookup and update flow
- JSON persistence for saved student records
- simple terminal styling for a clearer CLI experience

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

The core workflow is working:

- the app launches from the terminal
- student records can be checked and updated
- updates are written back to main/data.json

There is still room for improvement. The menu includes an option to list all data, but that flow is not implemented yet in the current codebase.

## Planned next steps

- add a proper "list all records" feature
- improve search and reporting options
- expand the registry with more student details
- explore more durable storage formats such as SQLite or CSV
- improve the CLI experience with clearer feedback and formatting

## Update log

- Latest update: July 25, 2026
