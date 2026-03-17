tasks = []

def add_task():
    name = input("Enter task name: ")
    due_date = input("Enter due date: ")
    priority = input("Enter priority (High/Medium/Low): ")
    status = "Pending"

    task = {
        "name": name,
        "due_date": due_date,
        "priority": priority,
        "status": status
    }

    tasks.append(task)
    print("Task added successfully!\n")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']}")
        print(f"   Due Date: {task['due_date']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {task['status']}\n")


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
    tasks[num-1]["status"] = "Completed"
    print("Task marked as completed.\n")


while True:

    print("===== Task List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Complete Task")
    print("5. Exit")

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
        print("Exiting program.")
        break

    else:
        print("Invalid option.\n")