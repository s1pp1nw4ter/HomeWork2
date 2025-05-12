from task_tracker import TaskStorage
from fastapi import FastAPI

app = FastAPI()
storage = TaskStorage()


@app.get("/tasks")
def get_tasks():
    return storage.get_all_tasks()


@app.post("/tasks")
def create_task(title: str):
    new_task = storage.create_new_task(title)
    return {f'Task is created: {new_task}'}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str, status: int):
    update_t = storage.update_task(task_id, title, status)
    if update_t is None:
        return {f'Your task is not exist!'}
    return {f'Task is updated: {update_t}'}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = storage.remove_task(task_id)
    if deleted is None:
        return f'Your task is not exist!'
    return {f'Task {deleted} was deleted!'}
