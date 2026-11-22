tasks = []
completed_tasks = []

def add_task():
    title = input("Enter task name: ")

    if not title.strip():
        print("Task name cannot be empty!")
        return

    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "priority": priority
    }

    tasks.append(task)
    print("Task added successfully!")



def view_tasks():
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No pending tasks!")
        return
    for task in tasks:
        print("Task:", task["title"])
        print("Priority:", task["priority"])
        print("Due Date:", task.get("due_date", "Not set"))
        print("----------------")


def delete_task():
    title = input("Enter task to delete: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            print("Task deleted!")
            return
    print("Task not found.")

def complete_task():
    title = input("Enter completed task: ")
    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            completed_tasks.append(task)
            print("Task completed!")
            return
    print("Task not found.")

def view_completed_tasks():
    print("\n--- Completed Tasks ---")
    if not completed_tasks:
        print("No completed tasks yet!")
        return
    for task in completed_tasks:
        print("Task:", task["title"])
        print("Priority:", task["priority"])
        print("----------------")

def add_due_date():
    title = input("Enter task name: ")
    for task in tasks:
        if task["title"] == title:
            due_date = input("Enter due date (DD-MM-YYYY): ")
            task["due_date"] = due_date
            print("Due date added!")
            return
    print("Task not found.")


def task_manager():
    while True:
        print("\n===== StudySync Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. View Completed Tasks")
        print("6. Add Due Date")
        print("7. Exit")
        choice = input("\nChoose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            view_completed_tasks()
        elif choice == "6":
            add_due_date()
        elif choice == "7":
            print("Thank you for using StudySync!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    task_manager()