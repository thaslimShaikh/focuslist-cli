def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

show_menu()

def view_tasks():
    with open("tasks.txt", "r") as f:
        for i, task in enumerate(f.readlines(), start=1):
            print(i, task.strip())
