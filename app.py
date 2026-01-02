def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + " | pending\n")
    print("Task added successfully")
