
# Task 1

# student_bio = {}

# name = input("Enter name: ").title()
# age = int(input("Enter age: "))
# gender = input("Enter gender: ").title()
# courses = input("Enter courses seperaed by spaces: ").title().split()

# student_bio["name"] = name
# student_bio["age"] = age
# student_bio["gender"] = gender
# student_bio["courses"] = courses
# print("--" * 10)
# print("Student bio data")
# print("--" * 10)
# print(f"Name\t: \t {student_bio["name"]} \nAge\t: \t {student_bio["age"]} \nGender\t: \t {student_bio["gender"]} \nCourse\t: \t {student_bio["courses"]}")
# print("--" * 10)


# Task 2

# super_market_p_list = {}

# items = ["pencil", "dettol","batteries","shoe","detergent"]
# prices = input("Enter prices of the item seperated by spaces: ").split()

# super_market_p_list["items"] = items
# super_market_p_list["price"] = prices

# print(super_market_p_list)
# print(super_market_p_list.keys())

# updated_prices = input("Enter updated prices of the item seperated by spaces: ").split()
# super_market_p_list.update({"price": updated_prices})
# print(super_market_p_list)

# Task 2

# super_market_p_list = {}

# items = ["pencil", "dettol","batteries","shoe","detergent"]

# user_price_1 = float(input("price of the first item: "))
# user_price_2 = float(input("price of the second item: "))
# user_price_3 = float(input("price of the third item: "))
# user_price_4 = float(input("price of the fourth item: "))
# user_price_5 = float(input("price of the fifth item: "))

# user_prices = [user_price_1, user_price_2, user_price_3, user_price_4, user_price_5]

# super_market_p_list["items"] = items
# super_market_p_list["user_prices"] = user_prices
# print(super_market_p_list)

#print("Enter the updated price ")
# new_user_price_1 = float(input("updated price of the first item: "))
# new_user_price_2 = float(input("updated price of the second item: "))
# new_user_price_3 = float(input("updated price of the third item: "))
# new_user_price_4 = float(input("updated price of the fourth item: "))
# new_user_price_5 = float(input("updated price of the fifth item: "))


# updated_prices = [new_user_price_1, new_user_price_2, new_user_price_3, new_user_price_4, new_user_price_5]

# super_market_p_list.update({"user_price": updated_prices})
# print(super_market_p_list)


# Task 3

days_of_the_week = ("Sunday", "Monday","Tuesday", "Wednesday","Thursday", "Friday")

print("Actiities for three days ")

day_1 = input("Enter day one activity: ")
day_2 = input("Enter day two activity: ")
day_3 = input("Enter day three activity: ")


act_for_days = [day_1, day_2, day_3]

days_and_activ_dict = {days_of_the_week : act_for_days in zip(days_of_the_week, act_for_days)
}

print(days_and_activ_dict)


# days_and_activ_dict = dict(zip(days_of_the_week, act_for_days))
# print(days_and _activ_dict)