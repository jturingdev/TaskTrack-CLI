import argparse
import argparse as arg
from pathlib import Path
import logging

from src.task.models.task import Status, Priority, Category
from src.task.service.controller import TaskManager

logging.basicConfig()
logger = logging.getLogger()

path = Path('/')

manager = TaskManager()


def main():
    ""
    if arg.ArgumentParser == True:
        cli_mode()
    else:
        interactive_mode()

def cli_mode():
    "argparse logic"
    parser = argparse.ArgumentParser(
        prog='TaskerTrackCLI',
        description='Management in Tasks',
        epilog='Text at the bottom of help'
    )
    parser.add_argument('task-cli''list', type=str, help='List a task')
    parser.add_argument('task-cli''list done', type=str, help='List a task')
    parser.add_argument('task-cli''list todo', type=str, help='List a task')
    parser.add_argument('task-cli''list in-progress', type=str, help='List a task')

    parser.add_argument('task-cli''mark-in-progress''id', type=str, help='List a task')
    parser.add_argument('task-cli''mark-done''id', type=str, help='List a task')

    parser.add_argument('task-cli''add''title''description''category''author''status''priority''term', type=str, help='Add a task')
    parser.add_argument('task-cli''update''id''title''description''category''author''status''priority''term', type=str, help='Update a task')
    parser.add_argument('task-cli''remove''id', type=str, help='Remove a task')
    args = parser.parse_args()
    if args == 'list':
        print(manager.list_tasks())
        if args == 'done':
            print(manager.list_tasks_status(args.status))
        elif args == 'todo':
            print(manager.list_tasks_status(args.status))
        elif args == 'in-progress':
            print(manager.list_tasks_status(args.status))
    elif args == 'mark':
        print(manager.mark_task())
    elif args == 'add':
        print(manager.add_task(args.title, args.description, args.category, args.status, args.priority, args.term))
    elif args == 'update':
        print(manager.update_task(args.option, ))
    elif args == 'remove':
        print(manager.delete())

def interactive_mode():
        while True:
            manager.list_tasks()
            options = "\n1. Add Task\n2. List Tasks\n3. Update\n4. Delete\nq. Exit"
            print(options)
            try:
                opc = input("\nSelect option: ")
                match opc:
                    case '1':
                        title = str(input())
                        desc = str(input())
                        cat = str(input(Category))
                        author = str(input())
                        status = str(input(Status))
                        priority = str(input(Priority))
                        manager.add_task(title, desc, cat, author, status, priority)
                    case '2':
                        manager.list_tasks_status()
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
