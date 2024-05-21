def task():
    tasks = []
    print('WELCOME TO TASK MANAGEMENT APP')
    
    total_task = int(input("Enter how many tasks you want to complete today: "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter Task {i}: ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    
    while True:
        print("\nMenu:")
        print("1 - Add a task")
        print("2 - Update a task")
        print("3 - Delete a task")
        print("4 - View tasks")
        print("5 - Exit")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
        
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task '{updated_val}' to '{up}'.")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            
            delete_val = input("Enter the task name you want to delete: ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted.")
            else:
                print(f"Task '{delete_val}' not found.")

        elif operation == 4:
            
            print(f"Today's tasks are:\n{tasks}")

        elif operation == 5:
            
            print("Exiting the Task Management App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


task()
#this is a task managing app in which 5 tasks can be added ,tasks can be updated or deleted just by pressing the respective numbers .