import datetime

def get_menu_selection(menu_items):
    """
    Display a menu and return the user's selection
    """
    print("\n")
    for menu_items in menu_items:
        print(menu_items)

    return input("\nPlease select an option from above.")

def display_selection_error(menu_selection):
    if menu_selection.isdigit():
        print("\n{} is an invalid option, please try again" .format(menu_selection))
    else:
        print("\n{} is not a number, please enter a number from the menu above" .format(menu_selection))

class Todo(): 

    def __init__(self, name):
        """ may not need name as argument """
        self.name = name
        self.master_list = []

    def add_task():
        pass

    def remove_task():
        pass

    def change_status():
        pass
        """ add later """

    def sort_master_list():
        pass
        """ add later """


class Tasks():

    def __init__(self, task_name, date, taskNumber):
        self.task_name = task_name
        self.date = date
        self.status = True
        self.taskNumber = taskNumber

class Display():

    MENU_ITEMS = (
       "1: Create list ",
       "2: Add new task",
       "3: Remove task",
       "4: View list",
       "0: Exit",
    )

    def display_main(self):
        taskNumber = 0

        while True:
            menu_selection = get_menu_selection(self.MENU_ITEMS)
            if menu_selection == "0":
                break
            elif menu_selection == "1":
                name = input("\nWhat would you like to name your list? ")
                todo = Todo(name)
                print(todo)
                print(todo.name)
                print(todo.master_list)
            elif menu_selection == "2":
                task_name = input("\nWhat is your task? ")
                date = datetime.datetime.now()
                taskNumber = taskNumber + 1
                task = Tasks(task_name, date, taskNumber)
                todo.master_list.append(task)
                print(task)
                print(task.task_name)
                print(task.date)
                print(task.taskNumber)
                print(task.status)
                print(todo.master_list)
            elif menu_selection == "3":
                pass
            elif menu_selection == "4":
                for item in todo.master_list:
                    # print(item.task_name)
                    print("{} : Task: {}  |  Date: {}  | Status: {}".format(item.taskNumber, item.task_name, item.date, item.status))
            else:
                display_selection_error(menu_selection)


def main():
    """
    Main Loop
    """

    display = Display()
    display.display_main()

if __name__ == '__main__':
    main()

