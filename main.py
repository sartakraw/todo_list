# make todo list now

def main():
    tasks = []
    while True:
        print("=========================")
        print("1. Add item to the todo list")
        print("2. Mark tasks as done")
        print("3. View tasks")
        print("4. Exit todo list ")

        choice = int(input("Choose an option: "))

        if choice == 1:
            new_task = input("Enter a task in the todo list: ")
            new_item = {new_task: "Not finished"}
            if tasks:
                for elements in tasks:
                    if new_task not in elements.keys():
                        tasks.append(new_item)
            else:
                tasks.append(new_item)

        elif choice == 2:
            task_no = int(input("Which task to mark as finished? Input the index number: "))
            task_name = input("Input the task name: ")
            if tasks[task_no-1] and task_name == str(tasks[task_no-1]):
                for items in tasks:
                    if task_name in items.keys():
                        tasks[task_no-1][task_name] = "finished"
                        print(items[task_no - 1])
                    else:
                        print("Wrong input")
            else:
                print("Wrong input")

        elif choice == 3:
            print("Tasks: \n")
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")

        elif choice == 4:
            print("Exiting the todo list.")
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
