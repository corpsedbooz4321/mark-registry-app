# 📈 Project Progress Tracker

This document records the current milestones of the Mark Registry App as it evolves from a simple terminal utility into a small student record system.

---

## 🚦 Quick Overview

- Current status: 🟢 Core CLI workflow is working
- Next milestone: 🟡 Improve data exploration and reporting features
- Target audience: small coaching institutes, tutors, and beginner Python learners

---

## 🗺️ Milestone Checklist

### 🟢 Phase 1: Modular CLI Workflow (Completed)

- [x] Create a CLI entry point in main/main.py.
- [x] Split lookup and update actions into dedicated modules:
  - [main/check.py](main/check.py) for result lookup
  - [main/update.py](main/update.py) for adding or updating marks
  - [main/data.json](main/data.json) for shared registry data
- [x] Add input validation for student names and mark values.
- [x] Allow multiple subject entries in one update session before saving.
- [x] Include sample student data to demonstrate the workflow.

### 🟢 Phase 2: JSON-Based Persistence (Completed)

- [x] Store student records in [main/data.json](main/data.json).
- [x] Save updates back to the registry file between runs.
- [x] Keep the CLI experience simple and lightweight.

### 🟡 Phase 3: CLI Enhancements (In Progress)

- [ ] Add a proper "list all records" feature from the main menu.
- [ ] Improve formatting and readability of result output.
- [ ] Add search and filtering options for larger registries.

### ⚪ Phase 4: Expanded Registry Features

- [ ] Add more student details such as subjects, exam dates, or attendance.
- [ ] Support richer reporting and summaries.
- [ ] Prepare the project for future UI or web-based access.

### ⚪ Phase 5: Advanced Persistence

- [ ] Explore SQLite or CSV as alternative storage formats.
- [ ] Improve data reliability and backup-friendly workflows.

---

## 📝 Recent Development Notes

- The app now has a functional menu-driven experience for checking and updating marks.
- Student data is persisted in [main/data.json](main/data.json), so updates remain available across runs.
- The current implementation is intentionally simple and focused on the core registry workflow.
- The menu contains a placeholder option for listing all data, but that feature is not yet implemented.

## Update log

- Latest update: July 25, 2026

---

**Last updated:** July 25, 2026
