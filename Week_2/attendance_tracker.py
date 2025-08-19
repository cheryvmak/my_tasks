
#T ask 6

days_of_the_week = ("Sunday", "Monday","Tuesday", "Wednesday","Thursday", "Friday")
months_of_the_year = ("January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December")
student_name = input("Enter the Student name: ")
gender = input("Enter the Student gender: ")
course_track = input("Enter the Student Course track: ")
current_month_no = int(input("Enter the current month number: "))
current_day_no = int(input("Enter the current day number: "))
print(f"{student_name}\t{gender}\t{course_track}\t{months_of_the_year[current_month_no - 1]}\t{days_of_the_week[current_day_no - 1]}")
print(f"{student_name} is a {gender} learning {course_track} on {days_of_the_week[current_day_no - 1]}, {months_of_the_year[current_month_no - 1]} 2025.")