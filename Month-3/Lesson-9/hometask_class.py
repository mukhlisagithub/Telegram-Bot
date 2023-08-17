
class ToDo:
    def __init__(self):
        self.tasks = []

    # def add_task(self, task):
    #     self.add_task(task)
    #     print("Task is added")

    def add_task(self, task):
        fayl = open('todo_list.txt', 'a')
        data = open('todo_list.txt', 'r')
        res = f'{len(data.readlines())+1} {task}'
        fayl.write(res + '\n')
        print('Task is added')

    def completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task is completed")
        else:
            print("Task is not found")

    def show_task(self):
        text = open('show.txt', 'a')
        f = open('show.txt', 'r')
        res = f'{len(text.readlines())+1}'
        text.write(res + '\n')
        print("show")






# if __name__ == "__main__":
todo_list = ToDo()
todo_list.add_task('go tho the gym')
# todo_list.add_task("Wake up early")
# todo_list.add_task("Do morning exercises")
# todo_list.add_task("Reading the book")
# todo_list.add_task("Cooking the meal")
# todo_list.add_task("Washing the dishes")
# todo_list.add_task("Cleaning the rooms")
# todo_list.add_task("Go to the course")
# todo_list.add_task("Have a shower")
# todo_list.add_task("Have a dinner")
# todo_list.add_task("Go to bed")

while True:
    text = input("Enter the text: ")
    if text == "stop":
        print("Good bye!")
        break
    elif text == "show":
        todo_list.show_task()
    elif text.startswith('add'):
        task = text.split('',1)[1]
        todo_list.add_task(task)
    elif text.startswith("completed"):
        task_number = int(text.split('',1)[1])
        todo_list.completed(task_number)



