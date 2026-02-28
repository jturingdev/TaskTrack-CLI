import os
import pathlib
from datetime import datetime
from enum import Enum
from pathlib import Path
import sys
import argparse
import json
import pandas as pd
import uuid
import logging
import typing
from io import StringIO

from pandas import DataFrame

logging.basicConfig()
logger = logging.getLogger()

path = Path('/')

class Task:
    def __init__(self, title, category, description, author) -> None:
        self.id = uuid.uuid4().__str__()
        self.title = title
        self.description = description
        self.category = category
        self.author = author
        self.status = "todo" # todo, in-progress, done
        self.createdAt = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.updateAt = self.createdAt

class Categoria(Enum):
    WORK = 'WORK'
    SCHOOL = 'SCHOOL'
    PERSONAL = 'PERSONAL'

class Status(Enum):
    TODO = 'TODO'
    PROGRESS = 'PROGRESS'
    DONE = 'DONE'

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logging.info("File not found")
            return []
        except FileExistsError:
            logger.error("File not Exists")

    def save_tasks(self):
        try:
            with open(self.filename, 'w', encoding="utf-8") as f:
                json.dump(self.tasks, f, indent=4)
                logger.info(f"{f} -- Saved")
        except FileExistsError:
            logger.error("Error save task File not Exists")
        except FileNotFoundError:
            logger.error("Error save task File not Found")

    def add_task(self, title, description, category, author):
        new_task = Task(title, description, category, author)
        task = vars(new_task)
        self.tasks.append(task)
        self.save_tasks()
        print(task)

    def list_tasks(self) -> pd.DataFrame:
        df = {}
        if not self.tasks:
            print("sem tarefas")
        for task in self.tasks:
            df = pd.DataFrame.from_dict(task, orient="index")
            print(df)
        return df

    def update_task(self):
        "Update Task"
        print(f"\n1. Title\n2. Description\n 3. Category\n 4.Author\n 5. Status")
        option = input()
        task_id = input(f"TaskID or Title?: ")
        for task in self.tasks:
            if task["id"] == task_id or task_id == task["title"]:
                    while True:
                        try:
                            match option:
                                case '1':
                                    new_title = input()
                                    task["title"] = new_title
                                    self.save_tasks()
                                    break
                                case '2':
                                    new_desc = input()
                                    task["desc"] = new_desc
                                    self.save_tasks()
                                    break
                                case '3':
                                    new_category = input()
                                    task["category"] =  new_category
                                    self.save_tasks()
                                    break
                                case '4':
                                    new_author  = input()
                                    task["author"]  = new_author
                                    self.save_tasks()
                                    break
                                case '5':
                                    new_status = input(Status)
                                    task["status"] = new_status
                                    self.save_tasks()
                                    break
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
                self.save_tasks()
                break
        print(self.tasks)

def main():
    ""
    manager = TaskManager()
    while True:
        options = "\n1. Add Task\n2. List Tasks\n3. Update\n4. Delete\nq. Exit"
        print(options)
        try:
            opc = input("\nSelect option: ")
            match opc:
                case '1':
                    title = str(input())
                    desc = str(input())
                    cat = str(input(Categoria))
                    author = str(input())
                    manager.add_task(title, desc, cat, author)
                case '2':
                    manager.list_tasks()
                case '3':
                    manager.update_task()
                case '4':
                    manager.delete()
                case 'q':
                    break
                case _:
                    print("Not a option")
        except ValueError as e:
            logging.error("error")
        except Exception as e:
            logging.warning("error")

if __name__ == "__main__":
    main()