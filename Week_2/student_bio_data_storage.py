# Task 1

student_bio = {}

name = input("Enter name: ").title()
age = int(input("Enter age: "))
gender = input("Enter gender: ").title()
courses = input("Enter courses seperaed by spaces: ").title().split()

student_bio["name"] = name
student_bio["age"] = age
student_bio["gender"] = gender
student_bio["courses"] = courses
print("--" * 10)
print("Student bio data")
print("--" * 10)
print(f"Name\t: \t {student_bio["name"]} \nAge\t: \t {student_bio["age"]} \nGender\t: \t {student_bio["gender"]} \nCourse\t: \t {student_bio["courses"]}")
print("--" * 10)
