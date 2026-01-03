def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + " | pending\n")
    print("Task added successfully")

def view_tasks():
    with open("tasks.txt", "r") as f:
        for i, task in enumerate(f.readlines(), start=1):
            print(i, task.strip())
