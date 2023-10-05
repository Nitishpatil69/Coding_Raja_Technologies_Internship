from datetime import datetime


tasks = []


task_id_counter = 1


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def add_task(description, priority, due_date):
    global task_id_counter
    while not is_valid_date(due_date):
        print("Invalid date format. Please use YYYY-MM-DD format for due dates.")
        due_date = input("Enter due date (YYYY-MM-DD): ")

    task = {
        'id': task_id_counter,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    task_id_counter += 1

def remove_task(task_id):
    task_to_remove = None
    for task in tasks:
        if task['id'] == task_id:
            task_to_remove = task
            break

    if task_to_remove:
        tasks.remove(task_to_remove)
    else:
        print("Invalid task ID. Task not found.")

def mark_task_completed(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as completed.")
            return
    else:
        print("Invalid task ID. Task not found.")

def list_tasks():
    for task in tasks:
        status = "Completed" if task['completed'] else "Pending"
        print(f"Task {task['id']}: {task['description']} | Priority: {task['priority']} | Due Date: {task['due_date']} | Status: {status}")


while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Quit")

    choice = input("Select an option: ")

    if choice == "1":
        description = input("Enter task description: ")
        priority = input("Enter task priority (high/medium/low): ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(description, priority, due_date)
    elif choice == "2":
        task_id = int(input("Enter the ID of the task to remove: "))
        remove_task(task_id)
    elif choice == "3":
        task_id = int(input("Enter the ID of the task to mark as completed: "))
        mark_task_completed(task_id)
        return_to_menu = input("Task marked as completed. Return to the main menu? (yes/no): ")
        if return_to_menu.lower() != "yes":
            break
    elif choice == "4":
        list_tasks()
    elif choice == "5":
        print("Exiting the application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
