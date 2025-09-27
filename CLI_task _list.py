import json
from datetime import datetime

FILENAME = "tasks.json"

def load_tasks(filename=FILENAME):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename=FILENAME):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def run():
    tasks = load_tasks()
    while True:
        command = input("Gimme a command. ('add', 'show', 'remove', or 'quit'): ")
        if command == 'add':
            task = input('Gimme a task, lil pup: ')
            tasks.append(task)
            print(f"'{task}' has been added to your lackluster list of tasks.")
        elif command == 'show':
            if not tasks:
                print("""This guy...
You didn't give me a task.""")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"Task {i}: {task}")
                print("That's it for now, brodie.")
        elif command == 'remove':
            if not tasks:
                print("You ain't give me a task to remove, FN")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"Task {i}: {task}")
                try:
                    task_num = int(input("Which task you wanna remove? "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Task '{removed}' has been removed from ya list.")
                    else:
                        print("You buggin'. That task ain't on the list.")
                except ValueError:
                    print("Bruh, that ain’t even a number.")
        elif command == 'quit':
            save_tasks(tasks)
            print('This was not fun for me. Free me from this hell.')
            break
        else: 
            print("You had three choices, and you chose poorly.")
            break
run()

