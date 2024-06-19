import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def to_dict (self):
        return{
            "description":self.description,
            "completed": self.completed
        }

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self,description):
        task=Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        try:
            self.tasks.pop(index)
            self.save_tasks()
        except IndexError:
            print("Error: Task index out of range.")

    def complete_task(self, index):
        try:
            self.tasks[index].completed = True
            self.save_tasks()
        except IndexError:
            print("Error: Task index out of range.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for i, task in enumerate(self.tasks):
            status = "done" if task.completed else "not done"
            print(f"{i}. {task.description} [{status}]")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                return [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error: JSON decode error. Starting with an empty task list.")
            return []