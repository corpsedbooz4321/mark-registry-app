# 📈 Project Progress Tracker

This document tracks the development milestones of the Mark Registry App as it evolves from a simple CLI utility into a more structured and persistent registry system.

---

## 🚦 Quick Overview

- **Current Status:** 🟢 Phase 1 Complete
- **Next Milestone:** 🟡 Data Persistence
- **Target Audience:** Small coaching institutes and independent tutors

---

## 🗺️ Milestone Checklist

### 🟢 Phase 1: Modular CLI Architecture (Completed)

- [x] Create a CLI entry point in main/main.py.
- [x] Split the workflow into dedicated modules:
  - [main/check.py](main/check.py) for result lookup.
  - [main/update.py](main/update.py) for updating marks.
  - [main/data.py](main/data.py) for shared registry data.
- [x] Add a milestone for using a modular file system so logic stays organized and easier to maintain.
- [x] Support basic input validation for student names and mark values.
- [x] Allow repeated update operations inside the same session without returning to the main menu.

### 🟡 Phase 2: Data Persistence (Next)

- [ ] Replace the in-memory registry with a persistent data store.
- [ ] Save and load data from JSON or SQLite.
- [ ] Keep the CLI workflow intact while making records durable.

### ⚪ Phase 3: Expanded Registry Features

- [ ] Add more student details such as subjects, exam dates, or attendance.
- [ ] Improve the CLI with better formatting and navigation.
- [ ] Add search and filtering capabilities.

### ⚪ Phase 4: Web or Desktop UI

- [ ] Introduce a lightweight web or desktop interface.
- [ ] Expose the registry through simple API endpoints or a GUI.
- [ ] Prepare the project for broader use beyond the terminal.

---

## 📝 Recent Dev Notes

- The project now uses a modular file system rather than keeping all logic in a single script.
- The current registry still lives in memory, so persistence is the next major milestone.
- The structure is intentionally simple and beginner-friendly, making it a solid base for future expansion.

---
**Last Updated:** July 15, 2026
