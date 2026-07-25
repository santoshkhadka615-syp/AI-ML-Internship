# Simple To-Do List (CLI)
# Tasks are saved in a text file so they don't disappear when you close the program.

FILENAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!\n")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Removed: {removed}\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== To-Do List ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.\n")


if __name__ == "__main__":
    main()