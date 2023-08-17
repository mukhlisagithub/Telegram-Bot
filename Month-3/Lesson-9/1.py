class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task is added")

    def completed(self, index):
        if index >= 1 and index <= len(self.tasks):
            deleted_task = self.tasks.pop(index-1)
            print(f'"{deleted_task}" task is deleted')
        else:
            print("Invalid index")

    def show_tasks(self):
        print("-----------------------------")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
        print("-----------------------------")

todo_list = ToDo()

while True:
    command = input("Input: ")
    if command == "stop":
        print("Good bye")
        break
    elif command.startswith("add"):
        task = command[4:].strip()
        todo_list.add_task(task)
    elif command.startswith("completed"):
        index = int(command[10:].strip())
        todo_list.completed(index)
    elif command == "show":
        todo_list.show_tasks()
    else:
        print("Invalid command")