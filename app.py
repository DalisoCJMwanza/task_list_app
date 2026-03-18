from datetime import datetime, timedelta

tasks = []

def get_next_due_date(due_date_str, repeat):
    due = datetime.strptime(due_date_str, "%Y-%m-%d")
    if repeat == "daily":
        due += timedelta(days=1)
    elif repeat == "weekly":
        due += timedelta(weeks=1)
    elif repeat == "monthly":
        month = due.month + 1
        year = due.year
        if month > 12:
            month = 1
            year += 1
        due = due.replace(year=year, month=month)
    return due.strftime("%Y-%m-%d")


def add_task():
    name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    print("Is this a recurring task?")
    print("  1. No")
    print("  2. Daily")
    print("  3. Weekly")
    print("  4. Monthly")
    repeat_choice = input("Choose option: ")

    repeat_map = {"1": "none", "2": "daily", "3": "weekly", "4": "monthly"}
    repeat = repeat_map.get(repeat_choice, "none")

    task = {
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending",
        "repeat": repeat
    }

    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        repeat_label = f" | Repeats: {task['repeat'].capitalize()}" if task["repeat"] != "none" else ""
        print(f"{i+1}. {task['name']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {task['status']}{repeat_label}\n")


def search_task():
    keyword = input("Enter task name to search: ")

    for task in tasks:
        if keyword.lower() in task["name"].lower():
            print("Task Found:")
            print(task)
            return

    print("Task not found.\n")


def complete_task():
    view_tasks()
    num = int(input("Enter task number to mark as completed: "))
    task = tasks[num - 1]
    task["status"] = "Completed"
    print("Task marked as completed.\n")

    # If recurring, automatically create the next occurrence
    if task["repeat"] != "none":
        next_due = get_next_due_date(task["due_date"], task["repeat"])
        new_task = {
            "name": task["name"],
            "due_date": next_due,
            "priority": task["priority"],
            "status": "Pending",
            "repeat": task["repeat"]
        }
        tasks.append(new_task)
        print(f"Recurring task rescheduled! Next due date: {next_due}\n")


def delete_task():
    if len(tasks) == 0:
        print("No tasks available to delete.\n")
        return

    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            print("Invalid task number.\n")
            return

        removed_task = tasks.pop(num - 1)
        print(f"Task '{removed_task['name']}' deleted successfully!\n")

    except ValueError:
        print("Please enter a valid number.\n")


while True:

    print("===== Task List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        search_task()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        delete_task()

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid option.\n")