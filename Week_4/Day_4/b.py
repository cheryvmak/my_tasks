



# # add
# # remove
# # view

# tasks = []

# def add_task(task):
#     tasks.append(task)
#     print(f"Task {task} added!")

# def remove_task(task):
#     if task in tasks:
#         tasks.remove(task)
#         print(f"Task removed {task} succcesfully!")
#     else:
#         print("Task not found!")

# def view_task():
#     if tasks:
#         print("Your Task:")
#         for i, task in enumerate(tasks, 1):
#             print(f"{i} . {task}")
#     else:
#         print("Task not in the list")

# def save_task(task):
#     from pathlib import Path
#     import csv
#     file_path = Path("Week_5")
#     file_path.mkdir()
#     with open(file_path, "w", newline = "", encoding = "utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerows(tasks)

# while True:

#     print("Menu :")
#     print("1.\tAdd\n2.\tRemove\n3.\tView")
#     choice = int(input("select one of the option(1/2/3):"))

#     if choice == 1:
#         task = input("Enter task:")
#         add_task(task)

#     elif choice == 2:
#         task = input("Enter task:")
#         remove_task(task)

        
#     elif choice == 3:
#         view_task()
#         break
        
#     else:
#         print("invalid choice")


# question 17

# import csv
# from datetime import datetime
# from pathlib import Path
# date
# category
# amount
# details
# store_expenses = {}

# date = datetime.today().strftime("%Y-%m-%d")
# category = input("Enter category:")
# amount = float(input("Enter amount:"))
# details = input("Enter details:")

# store_expenses["date"] = date
# store_expenses["category"] = category
# store_expenses["amount"] = amount
# store_expenses["details"] = details

# print(store_expenses)

# workspace = Path("workfile")
# #workspace.mkdir(exist_ok=True)
# csv_file = workspace / "expenses.csv"


# with open(csv_file, "a", newline ="", encoding = "utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow([category, amount, details])
#     print("Expenses added succesfully:")

 
    # with open(csv_file,"r" , newline = "", encoding = "utf-8") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print(row)
    #     print("This are your recorded expenses:")



# import csv
# from datetime import datetime
# from pathlib import Path

# def add_expenses(date, category, amount, details):
#     with open(csv_file, "a", newline ="", encoding = "utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerow([category, amount, details])
      

# def view_expenses():
#     try:
#         with open(csv_file, "r", newline ="", encoding = "utf-8") as f:
#             reader = csv.reader(f)
#             for row in reader:
#                 print(row)
#     except FileNotFoundError:
#         print("File is not present")
        
# workspace = Path("workfile")
# #workspace.mkdir(exist_ok=True)
# csv_file = workspace / "expenses.csv"

# store_expenses = {}

# date = datetime.today().strftime("%Y-%m-%d")
# category = input("Enter category:")
# amount = float(input("Enter amount:"))
# details = input("Enter details:")


# store_expenses["date"] = date
# store_expenses["category"] = category
# store_expenses["amount"] = amount
# store_expenses["details"] = details

# print("Expenses added succesfully:")
# add_expenses(date, category, amount, details)
# print("This is your recorded expenses:")
# view_expenses()


responses = {
    "heya"          :       "No worry urself joor.?",
    "hello"         :       "Hi! How can i help you?",
    "how are you"   :       "I'm just a chatbot, but I'm doing great!",
    "be"            :       "Hello! How can I assist you?",
    #"He"            :       "welcome!",
    "bye"           :       "Goodbye! Have a great day!"
}

while True:
    user_input = input("You: ").lower().strip()
    if user_input in responses:
        print(f"Chatbot: {responses[user_input]}")
     
        if user_input == "bye":
            break
    else:
        print("Chatbot: I'm sorry, I don't understand that.")




# responses = {
#     "hi": "Hello! How can I assist you?",
#     "hello": "Hi! How can I help you?",
#     "how are you": "I'm just a chatbot, but I'm doing great!",
#     "what is python": "Python is a programming language used for various applications.",
#     "where are you learning data science": "Sail Innovation Lab",
#     "what programming language are you learning?": "Python",
#     "bye": "Goodbye! Have a great day!"
# }

# # Infinite loop to keep the chatbot running
# while True:
#     # Get user input and convert it to lowercase for case-insensitive matching
#     user_input = input("You: ").lower().strip()

#     # Check if the input exists in the responses dictionary
#     if user_input in responses:
#         # Print the corresponding response
#         print(f"Chatbot: {responses[user_input]}")

#         # Exit the loop if the user says 'bye'
#         if user_input == "bye":
#             break
#     else:
#         # If input is not recognized, display a default message
#         print("Chatbot: I'm sorry, I don't understand that.")







