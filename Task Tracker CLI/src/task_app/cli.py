from typing import Optional
from .database import Database_manager
from .models import Task,TaskStatus
import typer



app = typer.Typer()
db = Database_manager()

@app.command()
def add(title: str,description:str = typer.Argument(""),due_date:Optional[str]= None):
    
    db.add_task(Task(id=None,title=title, description=description, status=TaskStatus.TODO.value, due_date=due_date))
    typer.echo(f"Task '{title}' added with status 'todo'.")


@app.command()
def update_status(id:int,status:str):

    valid_status = [s.value for s in TaskStatus]
    readable_status = ", ".join(valid_status)
    if status not in valid_status:
        typer.echo(f"Invalid status. Choose either of these [{readable_status}]")
        raise typer.Exit()
    
    
    db.update_status_task(id,status)

@app.command()
def list_task(status: Optional[str]= None):
    if status:
        valid_status = [s.value for s in TaskStatus]
        
        if status not in valid_status:
            typer.echo(f"Invalid status command. Try with these {valid_status}")
            raise typer.Exit()
    
    tasks = db.get_task_by_status(status)

    if not tasks:
        typer.echo('No task found.')
        return
    
    for task in tasks:
        typer.echo(f"{task[0]}. [{task[3]}] {task[1]}: {task[2]}")
    
@app.command()
def delete_task(id: Optional[int] = typer.Option(None, help="Task ID to delete")):
    if id:
        db.del_task(id)
        typer.echo(f"Task {id} deleted successfully.")
    else:
        confirm = typer.confirm("Are you sure you want to delete all tasks?")
        if confirm:
            db.del_task()
            db.vacuum()
            typer.echo("All tasks deleted and reset")
        else:
            typer.echo('Deletion cancelled')


if __name__ == '__main__':
    app()
