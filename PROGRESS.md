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

## Versioning

The following is a draft timeline of major releases inferred from the repository commit history. Minor or fix commits are intentionally omitted — only commits that introduced new features, refactors, or notable UX changes are listed. Please review and suggest any changes or tags you prefer.

- **v1.0.0** — Initial release: project scaffolding, basic CLI workflow, and README. (notable commits: `44ed2be`, `f0e617a`)
- **v1.1.0** — Core features and UI: added JSON-backed persistence (`main/maindata/data.json`), `check`/`update`/`view_all` features, banner and color helpers. (notable commits: `ade2b39`, `8b6ad74`, `4a958be`, `1049a8c`, `81b9bdc`)
- **v1.2.0** — Data refactor: replaced in-memory registry with JSON data handling and updated progress/README to reflect persistence changes. (notable commits: `c5a991a`, `6e482b4`, `6415438`)
- **v1.3.0** — Delete entry feature and menu improvements: implemented `delete_entry` functionality and related menu options. (notable commits: `5be40e1`, `a31aa68`, `479cd8a`)
- **v1.4.0** — UX polish and help: banner formatting improvements, color/formatting tweaks, and help/instructions added. (notable commits: `c53b958`, `0e61840`, `c8512f0`)

_Note:_ These version labels were inferred automatically from commit messages and file additions/changes. If you already have a different version mapping or want me to tag specific commits with release tags, tell me which commits correspond to which version and I will update this section accordingly.
