import pyttsx3
import json
import os

class TaskList:
    def __init__(engine):
        engine.tasks = []
        engine.engine = pyttsx3.init()
        engine.filename = "PATH TO YOUR /tasks.json"
        engine.load_tasks()  # Load tasks when starting

       

    def save_tasks(engine):
        """Save tasks to JSON file"""
        try:
            with open(engine.filename, 'w') as f:
                json.dump(engine.tasks, f, indent=2)
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(engine):
        """Load tasks from JSON file"""
        try:
            if os.path.exists(engine.filename):
                with open(engine.filename, 'r') as f:
                    engine.tasks = json.load(f)
                print("Previous tasks loaded successfully!")
            else:
                engine.tasks = []
        except (json.decoder.JSONDecodeError, Exception) as e:
            print(f"Error loading tasks: {e}")
            engine.tasks = []

    def add_task(engine):
        while True:
            try:
                task = input("Enter the task you need to do: ").strip()
                if not task:
                    print("Task cannot be empty. Please try again.")
                    continue
                
                priority = input("Enter the priority (1 is highest): ").strip()
                if not priority.isdigit() or int(priority) < 1:
                    print("Priority must be a positive number. Please try again.")
                    continue
                
                priority = int(priority)
                engine.tasks.append({"task": task, "priority": priority})
                engine.save_tasks()  # Save after adding new task
                engine.engine.say(f"Task added: {task}")
                engine.engine.runAndWait()
                return task
            
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

    def get_sorted_tasks(engine):
        return sorted(engine.tasks, key=lambda x: x['priority'])

    def view_tasks(engine):
        if not engine.tasks:
            print("No tasks added yet.")
            return
        
        print("\nCurrent tasks (sorted by priority):")
        sorted_tasks = engine.get_sorted_tasks()
        for idx, task in enumerate(sorted_tasks, start=1):
            print(f"{idx}. Priority {task['priority']}: {task['task']}")

    def remove_task(engine):
        if not engine.tasks:
            print("No tasks to remove.")
            return

        engine.view_tasks()
        sorted_tasks = engine.get_sorted_tasks()

        try:
            task_num = int(input("\nEnter the number of the task to remove (1 to {}): ".format(len(sorted_tasks))))
            if 1 <= task_num <= len(sorted_tasks):
                removed_task = sorted_tasks[task_num - 1]
                engine.tasks = [task for task in engine.tasks if task != removed_task]  # Remove correctly
                engine.save_tasks()  # Save after removing task
                print(f"Removed task: {removed_task['task']}")
                engine.engine.say(f"Removed task: {removed_task['task']}")
                engine.engine.runAndWait()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    task_list = TaskList()
    
    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View current tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            task_list.add_task()
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            task_list.remove_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
    
    # Final message
    sorted_tasks = task_list.get_sorted_tasks()
    tasks_text = ", ".join([t["task"] for t in sorted_tasks]) if sorted_tasks else "No tasks added."
    task_list.engine.say(f"Here are your tasks in priority order: {tasks_text}")
    task_list.engine.runAndWait()

if __name__ == "__main__":
    main()
