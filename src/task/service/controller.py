import argparse
from datetime import datetime
from logging import INFO
from src.task.app import args
from src.task.models.task import Task, Status
import logging
from src.task.repositories import json_repo

logger = logging.getLogger()
logging.basicConfig(level=INFO, filename="logs", datefmt="%d/%m/%Y %H:%M:%S")

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = json_repo.load_tasks(self.filename)

    def add_task(self, args: argparse.Namespace) -> None:
        arguments = vars(args)
        task_dict_param = map_dict_to_task_params(arguments)
        new_task = Task(title, description, category, author, status, priority, term)
        task = vars(new_task)
        self.tasks.append(task)
        created = json_repo.save_tasks(filename=self.filename, tasks=self.tasks)
        return task

    def list_tasks(self):
        task = {}
        if not self.tasks:
            logger.info("No Tasks")
        for task in self.tasks:
            task = task
        return task

    def list_tasks_status(self, args: argparse.Namespace):
        #status = input(Status).upper()
        task = {}
        for actual_task in self.tasks:
            if actual_task["status"] == Status.__contains__(status):
                while True:
                    try:
                        if actual_task["status"] == status:
                            task = actual_task
                            print(task)
                            break
                        elif actual_task["status"] == status:
                            task = actual_task
                            print(task)
                            break
                        elif actual_task["status"] == status:
                            task = actual_task
                            print(task)
                            break
                    except Exception as e:
                        logger.error(e)
        return task

    def mark_progress(self):
        pass

    def mark_done(self):
        pass

    def update_task(self, option, task_id, new_title, new_desc, new_category, new_author, new_status, new_priority) -> None:
        "Update Task"
        print(f"\n1. Title\n2. Description\n 3. Category\n 4.Author\n 5. Status")
        #option = input()
        #task_id = input(f"TaskID or Title?: ")
        for task in self.tasks:
            if task["id"] == task_id or task_id == task["title"]:
                    while True:
                        try:
                            match option:
                                case '1':
                                    task["title"] = new_title
                                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                                    json_repo.save_tasks(self.filename, self.tasks)
                                    break
                                case '2':
                                    task["desc"] = new_desc
                                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                                    json_repo.save_tasks(self.filename, self.tasks)
                                    break
                                case '3':
                                    task["category"] =  new_category
                                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                                    json_repo.save_tasks(self.filename, self.tasks)
                                    break
                                case '4':
                                    task["author"]  = new_author
                                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                                    json_repo.save_tasks(self.filename, self.tasks)
                                    break
                                case '5':
                                    task["status"] = new_status
                                    task["updatedAt"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                                    json_repo.save_tasks(self.filename, self.tasks)
                                    break
                                case '6':
                                    task['priority'] = new_priority
                                    task['updatedAt'] = datetime.now().strftime()
                                    json_repo.save_tasks(self.filename, self.tasks)
                                case _:
                                    print("Invalid Option")
                        except Exception as e:
                            logging.error("")

    def delete(self):
        "Delete Task"
        task_id = input("TaskID?: ")
        for task in self.tasks:
            if task_id == task["id"] or task_id == task["title"]:
                self.tasks.remove(task)
                logger.info(f"{task["title"]} -- Success Removed")
                json_repo.save_tasks(self.filename, self.tasks)
                break