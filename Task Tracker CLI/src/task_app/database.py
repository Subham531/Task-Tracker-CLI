import sqlite3 
from .models import TaskStatus

class Database_manager:
    def __init__(self,db_path = 'data.db'):
        self.connection = sqlite3.connect('db_path')
        self.cursor = self.connection.cursor
        
    def create_table(self):
        self.cursor.execute(
            '''
                CREATE TABLE task(
                
                    id INT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'todo',
                    created_at TEXT,
                    due_date TEXT
                )
            '''
        )

        self.connection.commit()
    

    def close(self):
        self.connection.close()



