# Simple To-Do List Application

tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete_task = int(input("Enter task number to delete: "))
            if 1 <= delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print(f"Task '{removed}' deleted.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
