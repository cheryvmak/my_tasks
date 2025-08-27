
employee = "General Employee"

def IT_department():
    employee = "Chris(Training))"
    print("Inside Training Department:", employee)

def Training_department():
    employee = "Chris(IT)"
    print("Inside IT department:", employee)
    
print("In Global Namespace:", employee) 
    
IT_department()
Training_department()

print("Length of 'Python':", len("Python")) 

a = lambda x: x ** 2
print(a(5))

b = lambda x, y : x + y
print(b(4, 3))


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)


students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
# Sort by age
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True)
print(students_sorted_descending)


students_sorted_alphabetically = sorted(students, key=lambda student: student[0])
print(students_sorted_alphabetically)



