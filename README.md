# ado.ai
O'Reilly Media Agentic AI for DevSecOps

This repository contains a small Python CLI example for managing a simple to-do list.

Files added in this change:

- `src/todo.py`: A minimal CLI using `argparse` with `add` and `list` commands.
- `tasks.json`: JSON file used to persist tasks.
- `requirements.txt`: Notes that no external dependencies are required.

Usage
-----

Install requirements (if any):

```bash
python -m pip install -r requirements.txt
```

Add a task:

```bash
python src/todo.py add "Buy milk"
```

List tasks:

```bash
python src/todo.py list
```

