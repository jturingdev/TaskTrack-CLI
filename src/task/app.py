import argparse
import argparse as arg
import sys
from pathlib import Path
import logging

from task.models.task import Status
from task.service.controller import TaskManager

logging.basicConfig()
logger = logging.getLogger()

path = Path('/')

manager = TaskManager()

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='TaskerTrackCLI',
        description='Management in Tasks',
        epilog='Text at the bottom of help'
    )
    return parser

parser = build_parser()

def main():
    sub = parser.add_subparsers(dest="command")

    list_tasks = sub.add_parser("list")
    list_tasks.add_argument('filter', choices=['all','todo','done','in-progress'], type=str, help='List a task')

    add_task = sub.add_parser("add")
    add_task.add_argument('title')
    add_task.add_argument('description')
    add_task.add_argument('category')
    add_task.add_argument('author')
    add_task.add_argument('status')
    add_task.add_argument('priority')
    add_task.add_argument('term', type=str, help='Add a task')

    mark_task = sub.add_parser("mark")
    mark_task.add_argument('id', type=int, help='List a task')
    mark_task.add_argument('status',choices=['done','in-progress'], type=str, help='List a task')

    update_task = sub.add_parser("update")
    update_task.add_argument("id", type=int)
    update_task.add_argument("--title")
    update_task.add_argument("--description")
    update_task.add_argument("--category")
    update_task.add_argument("--author")
    update_task.add_argument("--status")
    update_task.add_argument("--priority")
    update_task.add_argument("--term")


    remove_task = sub.add_parser("remove")
    remove_task.add_argument('id', type=int, help='Remove a task')

    args = parser.parse_args()

    if args.command == 'list':
        if args.filter == "all":
            print(manager.list_tasks())
        elif args.filter == 'done':
            print(manager.list_tasks_status(status=str(Status.DONE.name)))
        elif args.filter == 'todo':
            print(manager.list_tasks_status(status=str(Status.TODO.name)))
        elif args.filter == 'in-progress':
            print(manager.list_tasks_status(status=str(Status.PROGRESS.name)))

    elif args.command == 'mark':
        if args.status == "done":
            manager.mark_done(task_id=args.id)
        elif args.status == "in-progress":
            manager.mark_progress(task_id=args.id)

    elif args.command == 'add':
        manager.add_task(
            title=args.title,
            description=args.description,
            category=args.category,
            author=args.author,
            status=args.status,
            priority=args.priority,
            term=args.term
        )
        print(f"✅ Tarefa '{args.title}' adicionada com sucesso!")

    elif args.command == 'update':
            manager.update_task(
                task_id=args.id,
                title=args.title,
                desc=args.description,
                category=args.category,
                author=args.author,
                status=args.status,
                priority=args.priority,
                term=args.term
            )
    elif args.command == 'remove':
            manager.delete(task_id=args.id)

if __name__ == "__main__":
    main()