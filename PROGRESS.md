# 📈 Project Progress Tracker

## 🚦 Current Status

- Current development stage: Early-stage but functional CLI application
- Current stable release: Latest public release observed is v1.0.1
- Development branch status: Active repository branch is main
- Overall completion summary: The core student mark registry workflow is implemented and working, with persistent JSON storage and a menu-based terminal interface

---

## 🗺️ Roadmap

### ✅ Phase 1 — Initial CLI

- [x] Create a terminal-based entry point with a main menu
- [x] Add a help screen for app usage
- [x] Provide a simple, color-enhanced terminal interface

### ✅ Phase 2 — Registry Features

- [x] Add student lookup by name
- [x] Add/update marks for a student
- [x] Delete student entries
- [x] Remove individual subjects from a student record
- [x] View all stored student data
- [x] Calculate averages and display basic statistics
- [x] Validate names and marks before saving

### 🟡 Phase 3 — CLI Polish

- [x] Improve the user experience with formatted output and banners
- [ ] Improve readability for larger datasets and longer result lists
- [ ] Add stronger search and filtering capabilities

### ⚪ Phase 4 — Data Management

- [ ] Add CSV or spreadsheet-friendly export support
- [ ] Explore a more robust storage backend such as SQLite

### ⚪ Phase 5 — Web Application

- [ ] Build a web-based or API-based version of the registry
- [ ] Expand the system into a fuller student management platform

---

## 📦 Current Features

- Student lookup by name
- Add or update subject marks
- Delete entire student records
- Remove individual subjects from a record
- View all saved student data
- Calculate average marks for a student
- Show basic result statistics in the terminal
- Help menu and CLI instructions
- JSON-based persistence
- Input validation for names and marks
- Modular Python architecture

---

## 🏗 Project Architecture

The project is organized as a lightweight modular Python CLI application:

- features/ contains the app’s main actions: student lookup, updates, deletion, viewing, and help output
- ui/ contains banner and color helpers for terminal presentation
- utils/ contains reusable helper logic such as average calculation
- database/ contains the JSON storage file used to persist student records

The entry point is the main script in the repository root folder, which wires the menu options to the feature modules.

---

## 📊 Current Statistics

- Feature modules: 5
- Utility modules: 1
- UI modules: 2
- Storage backend: JSON file
- Primary language: Python
- Current release: v1.0.1
- Documentation files: README.md, PROGRESS.md
- Test suite: Not present in the repository

---

## 🚀 Future Plans

Based on the current project direction and the existing CLI workflow, the most likely next steps are:

- Improve reporting and result formatting for larger registries
- Add search and filtering for student records
- Support exporting records to CSV or spreadsheet-friendly formats
- Migrate from JSON storage to a more structured database system such as SQLite
- Develop a web-based interface or API while preserving the terminal tool

---

## 📝 Recent Milestones

- Built a working menu-driven CLI application for student mark management
- Added persistent storage so records remain available across runs
- Implemented lookup, update, delete, and view-all workflows
- Added average-based statistics and input validation
- Introduced a cleaner terminal experience with banners and colored output

---

## 📅 Last Updated

July 31, 2026
