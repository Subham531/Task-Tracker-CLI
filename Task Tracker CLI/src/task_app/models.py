from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime = None
    due_date: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
# class Task:
#     def __init__(self,id: int,title: str,status: TaskStatus = TaskStatus.TODO,description: str="Not provided",created_at: datetime=None,due_date: datetime=None):
#         self.id = id
#         self.title = title
#         self.status = status
#         self.description = description
#         self.created_at = created_at
#         self.due_date = due_date

#         if self.created_at is None:
#             self.created_at = datetime.now()
    

#     def __repr__(self):
#         return (f'Task(id = {self.id},title = {self.title},status = {self.status},description = {self.description},created_at = {self.created_at},due_date = {self.due_date})')
    
#     def __eq__(self,other):
#         if not isinstance(other,task):
#             return False

#         return (self.id == other.id and 
#                 self.title == other.title and
#                 self.status == other.status and
#                 self.description == other.description and
#                 self.created_at == other.created_at and
#                 self.due_date == other.due_date)



task1 =  Task(1, "Buy eggs","For 30g of proteins") 

task2 = Task(2, "Go to gym")

print(repr(task1))

