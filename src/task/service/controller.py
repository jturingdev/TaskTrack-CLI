from datetime import datetime
from logging import INFO
import logging

from task.models.task import Task, Status
from task.repositories import json_repo

logger = logging.getLogger()
logging.basicConfig(level=INFO, filename="logs", datefmt="%d/%m/%Y %H:%M:%S")

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = json_repo.load_tasks(self.filename)
        if self.tasks:
            Task.counter = max(t['id'] for t in self.tasks)
        else:
            Task.counter = 0

    def add_task(self, title, description, category, author, status, priority, term) -> dict:
        new_task = Task(
            title=title,
            description=description,
            category=category,
            author=author,
            status=status,
            priority=priority,
            term=term
        )
        task_data = vars(new_task)

        self.tasks.append(task_data)
        json_repo.save_tasks(filename=self.filename, tasks=self.tasks)
        return task_data

    def list_tasks(self) -> list:
        if not self.tasks:
            logger.info("No Tasks")
            return []
        return self.tasks

    def list_tasks_status(self, status) -> list:
        return [t for t in self.tasks if t["status"]==status]

    def mark_progress(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = Status.PROGRESS.name
                json_repo.save_tasks(filename=self.filename, tasks=self.tasks)

    def mark_done(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = Status.DONE.name
                json_repo.save_tasks(filename=self.filename, tasks=self.tasks)

    def update_task(self, task_id, **kwargs) -> bool:
        "Update Task"
        for task in self.tasks:
            if task["id"] == task_id:
                for key, value in kwargs.items():
                    if value is not None:
                        task[key]=value
                        print(f"Task: ID:{task_id} | {task[key]} -> {value} Updated Success")
                task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                json_repo.save_tasks(self.filename, self.tasks)
                logger.info(f"Task:{task_id} - {task["title"]} Updated Success")
                return True
        return False

    def delete(self, task_id):
        "Delete Task"
        for task in self.tasks:
            if task_id == task["id"]:
                self.tasks.remove(task)
                logger.info(f"{task["title"]} -- Success Removed")
                json_repo.save_tasks(self.filename, self.tasks)
                break