

# Task 1

'''' **Task1:  Create and Display**

- Ask the user to enter three favorite Nigerian dishes (one at a time).

 - Store them in a tuple called dishes.

- Print the tuple in a single line, separating items with commas.

- Use the \n escape sequence to print each dish on a new line. '''


fav_dish = []
fav_dish_1 = input("Enter your first Nigeria favorite dish: ")
fav_dish_2 = input("Enter your second Nigeria favorite dish: ")
fav_dish_3 = input("Enter your third Nigeria favorite dish: ")
print(fav_dish.append(fav_dish_1))
print(fav_dish.append(fav_dish_2))
print(fav_dish.append(fav_dish_3))
favor_dish = (tuple(fav_dish))
print(favor_dish)
print("\n".join(favor_dish))


# Task 2

''' **Task2: Tuple and Input**

- Ask the user for 5 best friends’ names.

- Store them in a tuple friends.

- Print the tuple in reverse order. '''



best_friend_name =  []
best_friend_1 =  input("Enter best friend's name 1: ")
best_friend_2 =  input("Enter best friend's name 2: ")
best_friend_3 =  input("Enter best friend's name 3: ")
best_friend_4 =  input("Enter best friend's name 4: ")
best_friend_5 =  input("Enter best friend's name 5: ")

print(best_friend_name.append(best_friend_1))
print(best_friend_name.append(best_friend_2))
print(best_friend_name.append(best_friend_3))
print(best_friend_name.append(best_friend_4))
print(best_friend_name.append(best_friend_5))
best_friend_name = tuple(best_friend_name)
print(best_friend_name)
Reversed_name = best_friend_name[::-1]
print(Reversed_name)



'''' **Task3: Tuple Operations**
- Create a tuple of 5 Nigerian states entered by the user.

  - Print the first state and last state.

  - Check if "Lagos" is in the tuple and print "Yes" or "No".

  - Print the number of states entered.
    - (Hint: use the tuple membership) '''


  #  Task 3

nigerian_state =  []
state_1 =  input("Enter state 1: ")
state_2 =  input("Enter state 2: ")
state_3 =  input("Enter state 3: ")
state_4 =  input("Enter state 4: ")
state_5 =  input("Enter state 5: ")

print(nigerian_state.append(state_1))
print(nigerian_state.append(state_2))
print(nigerian_state.append(state_3))
print(nigerian_state.append(state_4))
print(nigerian_state.append(state_5))
nigerian_state = tuple(nigerian_state)
print(nigerian_state)
print(nigerian_state[0:5:4])
print("Lagos" in nigerian_state)
print(len(nigerian_state))



'''' **Task4: Tuple Unpacking**
 - Ask a user for their;

  - First name

  - Age

  - Favorite color

  - Home town

  - Store them in a tuple profile and unpack into variables.

  - Print and use  escape sequence to align each piece of information nicely. '''

# Task 4

profile = []
first_name = input("Enter your first_name: ")
age = input("Enter your age: ")
fav_color = input("Enter your favorite color: ")
home_town = input("Enter your home town: ")
print(profile.append(first_name))
print(profile.append(age))
print(profile.append(fav_color))
print(profile.append(home_town))
print(profile)
updated_profile = tuple(profile)
print(updated_profile)


print(f"first_name:\t{updated_profile[0]}")
print(f"age:      \t{updated_profile[1]}")
print(f"fav_color:\t{updated_profile[2]}")
print(f"home_town:\t{updated_profile[3]}")



''' **Task5: Modify Tuple Indirectly**
Ask a user to enter three items for their shopping list.

  - Store in a tuple shopping_list.

  - Convert it to a list, then ask for two more items to add.

  - Convert back to a tuple and print the updated list using join() to display items separated by " | ".
'''

# Task 5

shopping_list = []
shopping_item_1 = (input("Enter shopping item 1: "))
shopping_item_2 = (input("Enter shopping item 2: "))
shopping_item_3 = (input("Enter shopping item 3: "))
print(shopping_list.append(shopping_item_1))
print(shopping_list.append(shopping_item_2))
print(shopping_list.append(shopping_item_3))
print(shopping_list)
my_shopping_list = tuple(shopping_list)
print(my_shopping_list)
new_shopping_list = (list(my_shopping_list))
print(new_shopping_list)
new_item_1 = input("Enter additional item 1: ")
new_item_2 = input("Enter additional item 2: ")
new_shopping_list.append(new_item_1)
new_shopping_list.append(new_item_2)
print(new_shopping_list)
updated_shopping_list = tuple(new_shopping_list)
print(updated_shopping_list)
print("|".join(updated_shopping_list))




''' **Task6: Attendance Tracker**
- Write a Python program that;

 - Stores the days of the week in a tuple.

 - Stores the months of the year in another tuple.

 - Asks the user to enter:

   - Student’s name

   - Gender

   - Course Track
   
   - Current month number (1-12)

   - Current day number (1-7)
'''

#Task 6

days_of_the_week = ("Sunday", "Monday","Tuesday", "Wednesday","Thursday", "Friday")
months_of_the_year = ("January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December")
student_name = input("Enter the Student name: ")
gender = input("Enter the Student gender: ")
course_track = input("Enter the Student Course track: ")
current_month_no = int(input("Enter the current month number: "))
current_day_no = int(input("Enter the current day number: "))
print(f"{student_name}\t{gender}\t{course_track}\t{months_of_the_year[current_month_no - 1]}\t{days_of_the_week[current_day_no - 1]}")
print(f"{student_name} is a {gender} learning {course_track} on {days_of_the_week[current_day_no - 1]}, {months_of_the_year[current_month_no - 1]} 2025.")