class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Incomplete"
                print(f"{i}. {task.description} - {status}")

    def mark_task_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.mark_as_completed()
            print(f"Marked task '{task.description}' as completed.")
        else:
            print("Invalid task number.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task(description)
            print("Task added successfully.")
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_completed(task_number)
        elif choice == "4":
            print("Quitting the task management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
