import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.task_app.database import Database_manager
from src.task_app.models import Task,TaskStatus


@pytest.fixture
def test_db():
    db = Database_manager(':memory:')
    yield db
    db.close()

def test_add_task(test_db):
    task = Task(id=None,title="Buy condom",description="To have sex")
    test_db.add_task(task)
    tasks = test_db.get_task_by_status()
    assert len(tasks) == 1
    assert tasks[0][1] == "Buy condom"

def test_del_task(test_db):
    task = Task(id=None,title="Test",description="Test")
    test_db.add_task(task)
    test_db.del_task(1)
    tasks = test_db.get_task_by_status()
    assert len(tasks) == 0

def test_update_status(test_db):
    task = Task(id=None,title="Test",description="Test")
    test_db.add_task(task)
    test_db.update_status_task(1,"done")
    tasks = test_db.get_task_by_status("done")
    assert len(tasks) == 1
