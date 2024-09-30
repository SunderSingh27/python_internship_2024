import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = {}

        self.task_name_label = tk.Label(root, text="Task Name:")
        self.task_name_label.pack()

        self.task_name_entry = tk.Entry(root)
        self.task_name_entry.pack()

        self.due_date_label = tk.Label(root, text="Due Date:")
        self.due_date_label.pack()

        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack()

        self.view_tasks_button = tk.Button(root, text="View Tasks", command=self.view_tasks)
        self.view_tasks_button.pack()

        self.task_list_text = tk.Text(root)
        self.task_list_text.pack()

    def add_task(self):
        task_name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()
        self.tasks[task_name] = due_date
        self.task_list_text.insert(tk.END, f"{task_name}: {due_date}\n")

    def delete_task(self):
        task_name = self.task_name_entry.get()
        if task_name in self.tasks:
            del self.tasks[task_name]
            self.task_list_text.delete(1.0, tk.END)
            for task, due_date in self.tasks.items():
                self.task_list_text.insert(tk.END, f"{task}: {due_date}\n")
        else:
            messagebox.showerror("Error", "Task not found!")

    def update_task(self):
        task_name = self.task_name_entry.get()
        new_due_date = self.due_date_entry.get()
        if task_name in self.tasks:
            self.tasks[task_name] = new_due_date
            self.task_list_text.delete(1.0, tk.END)
            for task, due_date in self.tasks.items():
                self.task_list_text.insert(tk.END, f"{task}: {due_date}\n")
        else:
            messagebox.showerror("Error", "Task not found!")

    def view_tasks(self):
        self.task_list_text.delete(1.0, tk.END)
        for task, due_date in self.tasks.items():
            self.task_list_text.insert(tk.END, f"{task}: {due_date}\n")


def main():
    root = tk.Tk()
    todo = ToDoList(root)
    root.mainloop()


if __name__ == "__main__":
    main()