import matplotlib.pyplot as plt 

todo_task = []
task_status = []

def addTask():
    task = input("Please enter task: ")
    if task.strip() == "":
        print("Task cannot be empty")
    else:
        todo_task.append(task)
        task_status.append("incomplete")
        print("Task added successfully!")

def viewTask():
    if len(todo_task) == 0:
        print("No tasks to display")
    else:
        print("\nYour ToDo List:")
        for i, (task, status) in enumerate(zip(todo_task, task_status), 1):
            print(f"{i}. {task} - Status: {status}")

def updateStatus():
    viewTask()
    if len(todo_task) > 0:
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            if 1 <= task_num <= len(todo_task):
                task_status[task_num - 1] = "complete"
                print("Task status updated successfully!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

def deleteTask():
    viewTask()
    if len(todo_task) > 0:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(todo_task):
                removed_task = todo_task.pop(task_num - 1)
                task_status.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

def visualize():
    if len(todo_task) == 0:
        print("No tasks to visualize")
        return
        
    categories = ["Complete", "Incomplete"]
    counts = [task_status.count("complete"), task_status.count("incomplete")]
    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts, color=['green', 'red'])
    plt.title("Task Status Visualization")
    plt.xlabel("Task Status")
    plt.ylabel("Number of Tasks")
    
    # Add count labels on top of bars
    for i, count in enumerate(counts):
        plt.text(i, count, str(count), ha='center', va='bottom')
    
    plt.show()

def main():
    while True:
        print("\n****WELCOME TO TODO APP CLI****")
        print("Choose an action to perform:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Delete Task")
        print("5. Visualize Tasks")
        print("6. Exit")

        try:
            option = int(input("\nEnter your choice (1-6): "))
            
            if option == 1:
                addTask()
            elif option == 2:
                viewTask()
            elif option == 3:
                updateStatus()
            elif option == 4:
                deleteTask()
            elif option == 5:
                visualize()
            elif option == 6:
                print("Thank you for using ToDo App!")
                break
            else:
                print("Invalid option! Please choose between 1-6")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()