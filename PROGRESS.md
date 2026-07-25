# 📈 Project Progress Tracker

This document tracks the development milestones of the Mark Registry App as it grows from a simple terminal utility into a more structured student record system.

---

## 🚦 Quick Overview

- **Current Status:** 🟢 Core CLI workflow complete
- **Next Milestone:** 🟡 Persistent storage
- **Target Audience:** small coaching institutes, tutors, and beginner Python learners

---

## 🗺️ Milestone Checklist

### 🟢 Phase 1: Modular CLI Workflow (Completed)

- [x] Create a CLI entry point in main/main.py.
- [x] Split lookup and update actions into dedicated modules:
  - [main/check.py](main/check.py) for result lookup
  - [main/update.py](main/update.py) for adding or updating marks
  - [main/data.json](main/data.json) for shared registry data
- [x] Add basic input validation for student names and mark values.
- [x] Allow repeated update operations inside the same session without returning to the main menu.
- [x] Include example student data to demonstrate the workflow.

### 🟡 Phase 2: Data Persistence (In Progress)

- [x] Establish JSON-backed persistence using `main/data.json`.
- [ ] Improve durability and optional storage formats such as SQLite or CSV.
- [ ] Keep the CLI experience intact while adding data reliability.

### ⚪ Phase 3: Expanded Registry Features

- [ ] Add more student details such as subjects, exam dates, or attendance.
- [ ] Improve the CLI with richer formatting and navigation.
- [ ] Add search and filtering capabilities.

### ⚪ Phase 4: Web or Desktop UI

- [ ] Introduce a lightweight web or desktop interface.
- [ ] Expose the registry through simple API endpoints or a GUI.
- [ ] Prepare the project for broader use beyond the terminal.

### ⚪ Phase 5: User Authentication

- [ ] Add CLI user login using Google OAuth.
- [ ] Protect student registry actions behind authenticated access.
- [ ] Store and refresh OAuth tokens securely for CLI sessions.

---

## 📝 Recent Development Notes

- The app now has a basic but functional menu-driven experience for checking and updating marks.
- The current registry is stored in `main/data.json`, so updates persist across runs.
- The JSON file is used as the active data store and is ready for future persistence work and reference.

## Update Log

- Latest update: July 25, 2026

---

**Last Updated:** July 25, 2026
