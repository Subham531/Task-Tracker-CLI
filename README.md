# Task Tracker CLI

A command-line application for managing tasks with status tracking, built with Python.

[project url](https://roadmap.sh/projects/task-tracker)

## Features

- ✅ **Add Tasks** - Create new tasks with title, description, and optional due date
- ✅ **View Tasks** - List all tasks or filter by status (todo, in_progress, done)
- ✅ **Update Status** - Change task status between todo, in_progress, and done
- ✅ **Delete Tasks** - Remove individual tasks or delete all tasks with confirmation
- ✅ **Database Management** - SQLite database with automatic table creation
- ✅ **Timestamps** - Automatic creation timestamps for all tasks

## Project Structure

```
Task Tracker CLI/
├── src/
│   ├── __init__.py
│   └── task_app/
│       ├── __init__.py
│       ├── cli.py           # CLI commands using Typer
│       ├── database.py      # SQLite database operations
│       └── models.py        # Task and TaskStatus models
├── tests/
│   ├── __init__.py
│   ├── test_db.py          # Database tests
│   └── test_models.py      # Model tests
├── data.db                 # SQLite database file
└── README.md
```

## Installation

### Prerequisites
- Python 3.11+
- pip

### Setup

1. **Clone or navigate to the project:**
```bash
cd Task\ Tracker\ CLI
```

2. **Install dependencies:**
```bash
pip3 install typer
```

## Usage

### Add a Task
```bash
python3 -m src.task_app.cli add "Task Title" "Task Description" --due-date "2026-12-31"
```

**Example:**
```bash
python3 -m src.task_app.cli add "Buy groceries" "Milk, eggs, bread"
```

### List Tasks

List all tasks:
```bash
python3 -m src.task_app.cli list-task
```

Filter by status:
```bash
python3 -m src.task_app.cli list-task --status todo
python3 -m src.task_app.cli list-task --status in_progress
python3 -m src.task_app.cli list-task --status done
```

**Output:**
```
1. [todo] Buy groceries: Milk, eggs, bread
2. [in_progress] Finish project: Complete all features
3. [done] Review code: Code review completed
```

### Update Task Status

Change a task's status:
```bash
python3 -m src.task_app.cli update-status 1 in_progress
```

Valid statuses: `todo`, `in_progress`, `done`

### Delete Tasks

Delete a specific task by ID:
```bash
python3 -m src.task_app.cli delete-task --id 1
```

Delete all tasks (with confirmation):
```bash
python3 -m src.task_app.cli delete-task
```

## API Reference

### Models

#### TaskStatus Enum
```python
class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'
```

#### Task Dataclass
```python
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: str = TaskStatus.TODO.value
    created_at: datetime = None
    due_date: datetime = None
```

### Database Operations

#### Database_manager Class
- `add_task(task)` - Add a new task
- `update_status_task(id, status)` - Update task status
- `get_task_by_status(status)` - Get tasks by status
- `del_task(id)` - Delete task by ID or all tasks if no ID
- `vacuum()` - Optimize database and reset autoincrement IDs
- `close()` - Close database connection

## Testing

Run all tests:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_models.py -v
pytest tests/test_db.py -v
```

Run with coverage:
```bash
pip3 install pytest-cov
pytest tests/ --cov=src -v
```

### Test Coverage
- **test_models.py** - Task model creation and default status
- **test_db.py** - Database operations (add, update, delete)

## Database Schema

### Tasks Table
```sql
CREATE TABLE task(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'todo',
    created_at TEXT,
    due_date TEXT
);
```

## Examples

### Complete Workflow

```bash
# Add new tasks
python3 -m src.task_app.cli add "Complete project" "Finish all features and testing"
python3 -m src.task_app.cli add "Code review" "Review pull requests"
python3 -m src.task_app.cli add "Documentation" "Write API documentation"

# View all tasks
python3 -m src.task_app.cli list-task

# Update status
python3 -m src.task_app.cli update-status 1 in_progress

# View in-progress tasks
python3 -m src.task_app.cli list-task --status in_progress

# Mark as done
python3 -m src.task_app.cli update-status 1 done

# Delete completed task
python3 -m src.task_app.cli delete-task --id 1

# View remaining tasks
python3 -m src.task_app.cli list-task
```

## Technologies Used

- **Python 3.11+** - Programming language
- **Typer** - CLI framework
- **SQLite** - Database
- **Pytest** - Testing framework
- **Dataclasses** - Data modeling

## Contributing

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Author

Created as a Python learning project for task management.

## Changelog

### Version 1.0.0 (2026-05-12)
- Initial release
- Task CRUD operations
- Status tracking
- Database persistence
- CLI interface with Typer
- Comprehensive test suite
