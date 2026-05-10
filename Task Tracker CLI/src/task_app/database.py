import sqlite3 
from .models import TaskStatus,Task

class Database_manager:
    def __init__(self,db_path = 'data.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        
    def create_table(self):
        self.cursor.execute(
            '''
                CREATE TABLE task(
                
                    id INT PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'todo',
                    created_at TEXT,
                    due_date TEXT
                );
            '''
        )
        self.connection.commit()


    def add_task(self,task):

        query  =  '''
                INSERT INTO task(title,description,status,created_at)
                VALUES(?,?,?,?);
        '''

        values = (
            task.title,
            task.description,
            task.created_at.isoformat(),
            task.due_date.isoformat()
        )

        self.cursor.execute(query,values)
        self.connection.commit()

    def update_status_task(self,id,status):
        
        query = '''
                UPDATE task
                SET status = ?
                WHERE id = ?
            '''
        
        self.cursor.execute(query,status,id)

        self.connection.commit()

    def get_task_by_status(self, status:str= None):

        if status:
            query = "SELECT * FROM task WHERE status = ?"
            self.cursor.execute(query,(status,))
        
        else:
            query = "SELECT * FROM task"
            self.cursor.execute(query)
        
        self.cursor.fetchall()


    def close(self):
        self.connection.close()



