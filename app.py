def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

show_menu()

def complete_task(index):
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    tasks[index] = tasks[index].replace("pending", "done")

    with open("tasks.txt", "w") as f:
        f.writelines(tasks)

    print("Task marked as done")

