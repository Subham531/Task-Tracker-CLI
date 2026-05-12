import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.task_app.models import Task,TaskStatus
from datetime import datetime

def test_task_creation():
    task = Task(id=1,title="Testing-task",description="Testing the description")
    assert task.title == "Testing-task"
    assert task.status == TaskStatus.TODO.value
    assert task.description == "Testing the description"

def test_task_default_status():
    task = Task(id=1,title="Test task")
    assert task.status == "todo"

