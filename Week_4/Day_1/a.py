for i in range(3):
    print(i)

zip()
names = ["Esther", "Precious", "Kennie"]
scores = [85, 90, 75]
for n, s in zip(names, scores):
    print(n, "scored", s)

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums)) # using map helps to applied the logic applied to each element of the array
print(squared)

nums = [1, 2, 3, 4]
even_nums = list(filter(lambda x: x % 2 == 0, nums)) # filter only applied to the only the element that the logic is been passed on.
print(even_nums)


Step 1: Input student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 + ": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# Step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("\nPerformance Summary:")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)


# Step 5: Ranking (using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True) # sort descending order
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):# The index position start from 1
    print(f"{rank}. {name} - {score}")

# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))


# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)

# Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)



Defining a function
def greet():
    print("Hello, welcome to AI Fellowship!")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()

Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to Python learning!")

# Calling with parameter- the actual name
greet("Class rep")
greet("Ridwan")

def greet(name):
    print("Hello", name)


# Function call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)


def add(a, b):
    return a + b

# Function call

result = add(4, 6)
print("The sum is:", result)

# Note the output and compare it with that of print()


def count_up_to(n):
    i = 1
    while i <= n:
        yield i   # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)

# Note the output: Instead of giving all numbers at once, the function yields them one at a time.



def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce("Ngozi", "AI Engineering")   # Correct order

# Change the arrangment and watch the output

introduce("AI Engineering","Ngozi")   # Incorrect order, this will throw a semantic error


def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# Change the arrangment and watch the output

introduce(track = "AI Engineering",name = "Ngozi")   # HEre you notice that order does not matter


def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track,".")

# function call
# Without specifying the default argument, but watch the ouput
introduce("Paul")  

introduce("Tunji Paul", track = "AI Development")


def add_numbers(*args): # non-keyword argument( single asterick) tuple
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call 
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)


def student_details(**kwargs):  # keyword argument( double astrick) dictionary
        for key, value in kwargs.items():
         print(key, ":", value)


# function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="Block Chain")


def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places

# ---------- LEts test ----------

# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))


