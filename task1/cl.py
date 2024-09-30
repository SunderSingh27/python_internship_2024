class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, due_date):
        self.tasks[task_name] = due_date
        print(f"Task '{task_name}' added successfully!")

    def delete_task(self, task_name):
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def update_task(self, task_name, new_due_date):
        if task_name in self.tasks:
            self.tasks[task_name] = new_due_date
            print(f"Task '{task_name}' updated successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available!")
        else:
            print("Available Tasks:")
            for task, due_date in self.tasks.items():
                print(f"{task}: {due_date}")


def main():
    todo = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            todo.add_task(task_name, due_date)
        elif choice == "2":
            task_name = input("Enter task name: ")
            todo.delete_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            new_due_date = input("Enter new due date: ")
            todo.update_task(task_name, new_due_date)
        elif choice == "4":
            todo.view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()