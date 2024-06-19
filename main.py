from todo import ToDoList

def display_menu():
    print("\nCommands:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Complete a task")
    print("4. List all tasks")
    print("5. Quit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        command = input("Enter a command (1-5): ")

        if command == "1":
            description = input("Enter a task description: ")
            todo_list.add_task(description)
        elif command == "2":
            try:
                index = int(input("Enter task index to remove: "))
                todo_list.remove_task(index)
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
        elif command == "3":
            try:
                index = int(input("Enter task index to mark as complete: "))
                todo_list.complete_task(index)
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
        elif command == "4":
            todo_list.list_tasks()
        elif command == "5":
            break
        else:
            print("Error: Unknown command. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
