# 📈 Project Progress Tracker

This document tracks the development milestones of the Student Mark Registry System as it evolves from a simple CLI script into a fully featured open-source web application.

---

## 🚦 Quick Overview

- **Current Status:** 🟢 Phase 1 Complete
- **Next Milestone:** 🟡 Phase 2 (Data Persistence)
- **Target Audience:** Small coaching institutes and independent tutors

---

## 🗺️ Milestone Checklist

### 🟢 Phase 1: Interactive CLI Architecture (Completed)

- [x] Create core logic to check if a name exists in a list (`name_check`).
- [x] Create logic to append new names to the data pool (`list_update`).
- [x] Build a master interactive menu (`menu`) to handle routing.
- [x] Implement a `while True` loop to keep the program running continuously.
- [x] **Feature Update:** Added a nested loop inside the update tool to allow batch-adding names smoothly without exiting to the main menu.
- [x] **UX Update:** Added string formatting (`\n`) for clean spacing and readability in the terminal.

### 🟡 Phase 2: Local Data Persistence (Up Next)

- [ ] Research Python's built-in `json` module.
- [ ] Replace the hardcoded list `l = [...]` with a local `students.json` file.
- [ ] Update `list_update()` to automatically save newly added names to the file.
- [ ] Update `name_check()` to load up-to-date names from the file every time it runs.

### ⚪ Phase 3: Relational Database Integration

- [ ] Migrate from JSON files to an **SQLite** database (built into Python).
- [ ] Expand the database structure (tables) to hold Student IDs, Subjects, and Exam Marks.
- [ ] Build basic SQL queries inside Python to add and filter marks.

### ⚪ Phase 4: Web Frontend & API Development

- [ ] Set up a lightweight **Flask** or **FastAPI** web server.
- [ ] Convert CLI prompts into backend routing endpoints (e.g., `/add-student`, `/results`).
- [ ] Create a clean, responsive frontend user interface using HTML and CSS.

### ⚪ Phase 5: Authentication & Public Deployment

- [ ] Add secure user logins (Separate dashboards for Teachers vs. Students).
- [ ] Deploy the application online for free hosting.
- [ ] Publish complete setup documentation so any small institute can deploy their own version from GitHub.

---

## 📝 Recent Dev Notes

* **Aha Moment:** Realized functions can be called seamlessly inside other functions (like triggering `menu()` inside `list_update()`) to control terminal flow and handle text spacing beautifully.

---
**Last Updated:** June 19, 2026
