# 📝 Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-03-15

### Added
- **CLI Interface**: Implemented `argparse` with subcommands (`add`, `list`, `update`, `mark`, `remove`).
- **Status Management**: Added CLI commands to mark tasks as `in-progress` or `done`.
- **Task Filtering**: Added ability to list tasks filtered by their current status (`todo`, `in-progress`, `done`).
- **Clean Architecture**: Restructured the project into separated layers (models, service/controllers, repositories).
- **Advanced Task Modeling**: Upgraded the `Task` entity to automatically generate unique identifiers (`UUID`) and timestamps (`createdAt`, `updatedAt`).

### Changed
- **Update Logic**: Refactored `TaskManager.update_task` to use `**kwargs` instead of positional arguments, allowing partial and dynamic field updates.

### Removed
- **Interactive Prompts**: Removed dynamic inputs and interactive terminal functions in favor of direct CLI arguments.

---

## [0.1.0] - Initial Release

### Added
- **Core Controller**: Implemented `TaskManager` to handle main business logic.
- **Basic CRUD**: Added operations to add, list, update, and remove tasks.
- **JSON Persistence**: Created `json_repo` (`load_tasks`, `save_tasks`) for local data storage.
- **Data Standardization**: Introduced Enums for `Status`, `Priority`, `Category`, and `Term` to strictly type task attributes.
- **Interactive Mode**: Added dynamic inputs and interactive functions for early testing and usage.