import sqlite3 
from .models import TaskStatus,Task

class Database_manager:
    def __init__(self,db_path = 'data.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()
        
    def create_table(self):
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS task(
                
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
                INSERT INTO task(title,description,status,created_at,due_date)
                VALUES(?,?,?,?,?);
        '''
    
        values = (
            task.title,
            task.description,
            task.status,
            task.created_at.isoformat() if task.created_at else None,
            task.due_date.isoformat() if task.due_date else None
        )

        self.cursor.execute(query,values)
        self.connection.commit()

    def update_status_task(self,id,status):
        
        query = '''
                UPDATE task
                SET status = ?
                WHERE id = ?
            '''
        
        self.cursor.execute(query,(status,id))

        self.connection.commit()

    def get_task_by_status(self, status:str= None):

        if status:
            query = "SELECT * FROM task WHERE status = ?"
            self.cursor.execute(query,(status,))
        
        else:
            query = "SELECT * FROM task"
            self.cursor.execute(query)
        
        return self.cursor.fetchall()

    def del_task(self, id:int = None):

        if id:
            query = "DELETE FROM task WHERE id = ?"

            self.cursor.execute(query,(id,))
        
        else:
            query = "DELETE FROM task"
            self.cursor.execute(query)

            self.cursor.execute("DELETE FROM sqlite_sequence WHERE name='task'")
        
        self.connection.commit()

    def vacuum(self):
        self.cursor.execute("VACUUM")
        self.connection.commit()

    def close(self):
        self.connection.close()



