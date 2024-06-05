Creating a To-Do List application in Python can be a fun and rewarding project! Here's a simple example of a command-line To-Do List application in Python:

python
# Define an empty dictionary to store tasks
tasks = {}

# Function to add a task
def add_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    tasks[task_name] = task_description
    print("Task added successfully!")

# Function to update a task
def update_task():
    task_name = input("Enter the task name you want to update: ")
    if task_name in tasks:
        new_description = input("Enter the new description: ")
        tasks[task_name] = new_description
        print("Task updated successfully!")
    else:
        print("Task not found!")

# Function to display all tasks
def display_tasks():
    if tasks:
        for task_name, task_description in tasks.items():
            print(f"{task_name}: {task_description}")
    else:
        print("No tasks found.")

# Main loop
while True:
	print("\n1. Add Task\n2. Update Task\n3. Display Tasks\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        update_task()
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
