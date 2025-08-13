
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