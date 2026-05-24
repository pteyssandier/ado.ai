import argparse
import json
import os
import sys
from datetime import datetime, UTC


TASKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tasks.json")


def load_tasks(path=TASKS_FILE):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, path=TASKS_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(text, path=TASKS_FILE):
    tasks = load_tasks(path)
    task = {
        "id": (tasks[-1]["id"] + 1) if tasks else 1,
        "text": text,
        "done": False,
        "created_at": datetime.now(UTC).isoformat(),
    }
    tasks.append(task)
    save_tasks(tasks, path)
    print(f"Added task #{task['id']}: {task['text']}")


def list_tasks(path=TASKS_FILE):
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "x" if t.get("done") else " "
        print(f"[{status}] {t['id']}: {t['text']}")


def build_parser():
    parser = argparse.ArgumentParser(prog="todo", description="Simple todo CLI")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("text", nargs="+", help="Task description")

    p_list = sub.add_parser("list", help="List tasks")

    return parser


def main(argv=None):
    argv = argv or sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "add":
        text = " ".join(args.text)
        add_task(text)
    elif args.cmd == "list":
        list_tasks()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
