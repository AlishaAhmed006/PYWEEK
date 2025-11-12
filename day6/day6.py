#to do list
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#BASEMODEL-BASE WHAT OUT API SHOULD DETECT
app=FastAPI()#swich on
class Todo(BaseModel):
    id:int
    task:str
    completed:bool=False
todos={
    Todo(id=1, task="clean the bed", completed=False),
    Todo(id=2, task="complete the assignment", completed=False),
    Todo(id=3, task="make dinner", completed=False)
}
@app.post("/todos")
def create_todo(task: str):
    new_id=len(todos)+1
    new_todo=Todo(id=new_id, task=task, completed=False)
    todos.append(new_todo)
    return new_todo

#reading all todos
@app.get("/todos")
def view_todos():
    return todos

#reading specific task
@app.get("/todos/{todo_id}")
def get_one_todo(todo_id:int):
    for todo in todos:
        if todo_id==todo.id:
            return todo
    raise HTTPException(status_code=404, detail="todo not found")

# edit a task
@app.put("/todo/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index, todo in enumerate(todos):
        if(todo.id==todo_id):
            todo[index]=updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="todo id not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            deleted_todo=todos.pop(index)
            return {"message":"todo deleted successfully", "todo":deleted_todo}