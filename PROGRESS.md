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
  - [main/data.py](main/data.py) for shared registry data
- [x] Add basic input validation for student names and mark values.
- [x] Allow repeated update operations inside the same session without returning to the main menu.
- [x] Include example student data to demonstrate the workflow.

### 🟡 Phase 2: Data Persistence (In Progress)

- [ ] Replace the in-memory registry with a persistent data store.
- [ ] Save and load data from JSON or SQLite.
- [ ] Keep the CLI experience intact while making records durable.

### ⚪ Phase 3: Expanded Registry Features

- [ ] Add more student details such as subjects, exam dates, or attendance.
- [ ] Improve the CLI with richer formatting and navigation.
- [ ] Add search and filtering capabilities.

### ⚪ Phase 4: Web or Desktop UI

- [ ] Introduce a lightweight web or desktop interface.
- [ ] Expose the registry through simple API endpoints or a GUI.
- [ ] Prepare the project for broader use beyond the terminal.

---

## 📝 Recent Development Notes

- The app now has a basic but functional menu-driven experience for checking and updating marks.
- The current registry is still stored in memory, so restarting the app will reset the sample dataset.
- A JSON example file is present for future persistence work and reference.

---

**Last Updated:** July 25, 2026
