
class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task is added")

    def completed(self, task):
        if task >= 1 and task <= len(self.tasks):
            deleted_tasks = self.tasks.pop(task-1)
            print(f"{deleted_tasks}" "Task is deleted")
        else:
            print("Invalid task")

    def show_tasks(self):
        print("--------------")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}.{task}")
        print("-----------")

todo_list = ToDo()

while True:
    text = input("Input: ")
    if text == "stop":
        print("Good Bye!")
        break
    if text.startswith("add"):
        task = text[4:].strip()
        todo_list.add_task(task)
    elif text.startswith("completed"):
        task = int(text[10:].strip())
        todo_list.completed(task)
    elif text == "show":
        todo_list.show_tasks()
    else:
        print("Invalid task")
