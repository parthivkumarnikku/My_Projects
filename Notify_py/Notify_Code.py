
import calendar

class Task:
    def __init__(self, taskname, category):
        self.taskname = taskname
        self.category = category
        
#Class for taskmanager..containing all the functions that our task manager provides-----------------------
        
class TaskManager:
    MAX_TASKS = 100

#Function to check validations(Valid yesr , Valid month, Valid day, and to check leap year)------------------------------------------
    
#This function initiates the taskslist
    def __init__(self):
        self.tasks = []
        self.task_counter = 0

    def is_valid_year(self, year):
        return year > 0

    def is_valid_month(self, month):
        return 1 <= month <= 12

    def is_valid_day(self, day):
        return 1 <= day <= 31

    def leap_year(self, year):
        if self.is_valid_year(year):
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        else:
            print("Please enter a valid year")
            
#Function to create task------------------------------------------------------------------------
            
    def create_task(self, task_name, category):
        if self.task_counter >= self.MAX_TASKS:
            print("Task limit reached.")
            return

        self.tasks.append(Task(task_name, category))
        self.task_counter += 1
        print("Task created successfully.")
        self.save_tasks()
        
#We can create task normally or to a particular date... We have given options where the first option tells to create task normally and the second option creates task for a particular date
    def create_task_option(self):
        print("\n")
        print("###########################################")
        print("\n")
        print("Create Task:")
        print("1. Create task normally")
        print("2. Create task for a particular date")
        
        print("\n")
        choice = int(input("Enter your choice: "))
        print("\n")
        
        #Option 1 -to create task normally--------------------
        
        if choice == 1:
       
            task_name = input("Enter the task name: ")
            print("\n")
            category = int(input("Enter the category (1: work, 2: important, 3: general): "))
            print("\n")
            self.create_task(task_name, category)

        #Option 2- to create task for a particular date-----------
            
        elif choice == 2:
            year = int(input("Please enter the year(xxxx): "))
            print("\n")
            if not self.is_valid_year(year):
                print("\n")
                print("Please enter a valid year.")
                print("\n")
                return
            month = int(input("Please enter the month(1-12): "))
            print("\n")
            day = int(input("Please enter the day(1-31): "))
            print("\n")
            self.create_task_for_date(year, month, day)
            print("\n")
        else:
            print("\n")
            print("Invalid choice. Task creation canceled.")
            print("\n")
            
#Function to list tasks: This function lists tasks already created with their corresponding date and category if available------------------------------------------------
    def list_tasks(self):
        if self.task_counter == 0:
            print("No tasks available.")
            return

        print("Tasks:")
        for i, t in enumerate(self.tasks, 1):
            categories = ["unknown", "work", "important", "general"]
            print(f"{i}. Category: {categories[t.category]}, Task: {t.taskname}")
            
#Function to edit tasks---------------------------------------------------------------
    def edit_task(self):
        if self.task_counter == 0:
            print("No tasks available to edit.")
            return

        task_index = int(input("Enter the index of the task to edit: "))
#We can edit three things in a task, we can edit the task name or the category or the date of the corresponding task------------
        if 1 <= task_index <= self.task_counter:
            print("What would you like to edit?")
            print("1. Task Name")
            print("2. Category")
            print("3. Date")

            edit_choice = int(input("Enter your choice: "))
            
            #Option 1: Editing task name------------------------------------------------------
            
            if edit_choice == 1:
                self.tasks[task_index - 1].taskname = input("Enter the new task name: ")

            #Option 2: Editing task category---------------------------------------------------
                
            elif edit_choice == 2:
                new_category = int(input("Enter the new category (1: work, 2: important, 3: general): "))
                self.tasks[task_index - 1].category = new_category

            #Editing task date---------------------------------------------------------------
                
            elif edit_choice == 3:
                print("Note: Editing date will remove existing date and replace it with the new one.")
                year = int(input("Please enter the year(xxxx): "))
                if not self.is_valid_year(year):
                    print("Please enter a valid year.")
                    return
                month = int(input("Please enter the month(1-12): "))
                day = int(input("Please enter the day(1-31): "))
                self.tasks[task_index - 1].taskname = f"{year:04d}-{month:02d}-{day:02d} {self.tasks[task_index - 1].taskname.split(' ', 1)[1]}"
            else:
                print("Invalid choice.")
                return

            print("Task edited successfully.")
            self.save_tasks()
        else:
            print("Invalid task index.")
            
#Function to delete tasks: Before deleting all the tasks will be listed and user can choose the index of the task they want to delete-----------------------------------------------------------------
    def delete_task(self):
        if self.task_counter == 0:
            print("No tasks available to delete.")
            return

        task_index = int(input("Enter the index of the task to delete: "))

        if 1 <= task_index <= self.task_counter:
            self.tasks.pop(task_index - 1)
            self.task_counter -= 1
            print("Task deleted successfully.")
            self.save_tasks()
        else:
            print("Invalid task index.")
            
#Function to create task for a particular date: This function create tasks for a particular date---------------------------------------------
            
    def create_task_for_date(self, year, month, day):
        if self.task_counter >= self.MAX_TASKS:
            print("Task limit reached.")
            return
        if not self.is_valid_month(month) or not self.is_valid_day(day):
            print("Please enter valid inputs.")
            return

        task_name = f"{year:04d}-{month:02d}-{day:02d} {input('Enter the task name: ')}"
        category = int(input("Enter the category (1: work, 2: important, 3: general): "))

        self.tasks.append(Task(task_name, category))
        self.task_counter += 1
        print("Task created successfully.")
        self.save_tasks()
        self.print_calendar(year, month)
        
#Function to display tasks for a particular date: After entering the date, it displays the tasks of that corresponding date if available or else it displays no tasks available for the particualr date-------------------------------------------------
        
    def display_tasks_for_date(self, year, month, day):
        print(f"Tasks for {year:04d}-{month:02d}-{day:02d}:")
        found = False

        for t in self.tasks:
            task_date = t.taskname.split()[0]
            if task_date == f"{year:04d}-{month:02d}-{day:02d}":
                found = True
                categories = ["unknown", "work", "important", "general"]
                print(f"Task: {t.taskname}, Category: {categories[t.category]}")

        if not found:
            print("No tasks found for the given date.")
            
#Function to save tasks: This function saves the tasks in the file , even after terminating the tasks are saved properly-----------------------------------------------------------------------
            
    def save_tasks(self):
        with open("tasks.txt", "w") as fp:
            fp.write(f"{self.task_counter}\n")
            for t in self.tasks:
                fp.write(f"{t.taskname} {t.category}\n")
                
#Function to load tasks: This function loads the previously saved tasks from the saved file ----------------------------------------------------------------------
                
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as fp:
                content = fp.readlines()

            if content:
                self.task_counter = int(content[0].strip())
                self.tasks = []  # Clear existing tasks before loading from the file
                for line in content[1:]:
                    task_info = line.strip().rsplit(' ', 1)
                    if len(task_info) == 2:
                        self.tasks.append(Task(task_info[0], int(task_info[1])))
        except FileNotFoundError:
            print("File not found: tasks.txt")
        except Exception as e:
            print(f"Error loading tasks: {e}")

#Function to print calender----------------------------------------------------------------------

    def print_calendar(self, year, month):
        days_in_month = calendar.monthrange(year, month)[1]
        print(f"Calendar for {year}-{month:02d}:")
        print("Sun Mon Tue Wed Thu Fri Sat")

        weekday = calendar.weekday(year, month, 1)
        for i in range(weekday):
            print("   ", end=" ")  

        day_counter = 1
        while day_counter <= days_in_month:
            print(f"{day_counter:3}", end=" ")
            weekday = (weekday + 1) % 7
            if weekday == 0:
                print()
            day_counter += 1
        print()
        
#Main function----------------------------------------------------------------------------------------------
        
def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\n")
        print("#########################     MENU     ############################")
        print("\n")
        print("What would you like to view now? (Enter your choice)")
        print("1. Calendar")
        print("2. Check if a year is a leap year or not")
        print("3. Tasks")
        print("4. Exit Notification center")
        print("\n")

        choice = int(input("Enter your choice: "))
        print("\n")
        
#Calender-option 1 -----
        if choice == 1:
            print("Option 1 ------------>  selected")
            year = int(input("Please enter the year(xxxx): "))
            if not task_manager.is_valid_year(year):
                print("Please enter a valid year.")
                print("\n")
                continue  

            month = int(input("Please enter the month(1-12): "))
            print("\n")
            if task_manager.is_valid_month(month):
                task_manager.print_calendar(year, month)
            else:
                print("Please check the month entered and enter valid inputs")
                
#Leap year -option 2-----
        elif choice == 2:
            print("Option 2 selected")
            print("\n")
            year = int(input("Please enter the year(xxxx): "))
            print("\n")
            if not task_manager.is_valid_year(year):
              print("Please enter a valid year.")
              print("\n")
              continue
            if task_manager.leap_year(year):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")

#Tasks-option 3:This option manages all the functions related to the tasks-----
                
        elif choice == 3:
            print("Option 3 selected")
            tasks_choice = 0
            while tasks_choice != 6:
                print("\n")
                print("################     TASK MENU     ##################")
                print("What would you like to do?")
                print("1. Create a task")
                print("2. Edit an existing task")             
                print("3. Display tasks corresponding to a date")
                print("4. Delete a task")
                print("5. List Tasks")
                print("6. Quit Task Manager")
                print("\n")
                tasks_choice = int(input("Enter your choice: "))
                
                #Create tasks -------------------------------------------------
                
                if tasks_choice == 1:
                    task_manager.create_task_option()

                #Editing an existing task:It first lists the available tasks and we choose which task to edit and we even choose what to edit , the taskname,or the category or the date of the task-------------   
                elif tasks_choice == 2:
                    print("Available Tasks:")
                    task_manager.list_tasks()
                    task_manager.edit_task()

                #It displays tasks corresponding to a particular date--------------------    
                elif tasks_choice == 3:
                    year = int(input("Please enter the year(xxxx): "))
                    if not task_manager.is_valid_year(year):
                        print("Please enter a valid year.")
                        continue
                    month = int(input("Please enter the month(1-12): "))
                    day = int(input("Please enter the day(1-31): "))
                    if task_manager.is_valid_month(month) and task_manager.is_valid_day(day):
                        task_manager.display_tasks_for_date(year, month, day)
                    else:
                        print("Please enter valid inputs")
                        
                 #It first lists the available tasks and we choose which task to delete------
                        
                elif tasks_choice == 4:
                    print("Available Tasks:")
                    task_manager.list_tasks()
                    task_manager.delete_task()

                #It lists the available tasks-------------------------------------------
                    
                elif tasks_choice == 5:
                    task_manager.list_tasks()
                    
                elif tasks_choice == 6:
                    print("\n")
                    print("Exiting task manager...")
                    
                else:
                    print("\n")
                    print("Invalid choice. Please try again.")
                    print("\n")
                    
        elif choice == 4:
            print("\n")
            print("Exiting Notification center...")
            print("\n")
            break

        else:
            print("\n")
            print("Invalid choice. Please try again.")
            print("\n")
    task_manager.save_tasks()

if __name__ == "__main__":
    main()
