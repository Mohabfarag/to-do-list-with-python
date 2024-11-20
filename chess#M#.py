import os

# Function to display the menu options
def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Completed")
    print("5. Exit")

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    return []

# Function to save tasks to a file
def save_tasks(filename, tasks):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a new task
def add_task(tasks):
    task = input("Enter the new task: ")
    tasks.append(f"[ ] {task}")
    print(f"Task '{task}' added.")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task[4:]}' removed.")
    else:
        print("Invalid task number.")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        if task.startswith("[x]"):
            print("This task is already completed.")
        else:
            tasks[task_index] = "[x] " + task[4:]
            print(f"Task '{task[4:]}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            mark_completed(tasks)
        elif choice == '5':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
