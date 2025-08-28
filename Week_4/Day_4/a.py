

# creating a folder and putting file in the folder

# library 
from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok = True)
# file_path = workspace / "notes.txt"
# print(file_path)


# creating file

# # create or overwrite using 'w'
# f = open(file_path, "w", encoding = "utf-8")
# f.write("This is the first line in notes.txt\n")
# f.close()

# (B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

# Open a file

# f = open(file_path, "w", encoding = "utf-8")
# f.write("Replace the old content with this line.\n")
# f.close()

# Write to a file

# f = open(file_path, "w", encoding = "utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()


# Append to a file 

# f = open(file_path, "a", encoding = "utf-8")
# f.write(" - Groundnut oil\n")
# f.write(" - Maggi\n")
# f.close()


# Read from a file

#  read() --- This read the whole file as one string
#  read(n) --- This read the number of character
#  readline() -- This read just one line at a time
#  readlines() -- list of all lines i.e all lines in one list

#  read() --- This read the whole file as one string and return everything the way it is writting
# f = open( file_path, "r", encoding = "utf-8")
# content = f.read()
# f.close
# print(content)

#  read(n) --- This read the number of character
# f = open(file_path, "r", encoding ="utf-8")
# content = f.read(40)
# f.close()
# print(content)


# readline() -- This read and bring output one at a time
# f = open(file_path, "r", encoding = "utf-8")
# print("first line:", f.readline().rstrip())
# print("second line:", f.readline().rstrip())
# f.close()


#  readlines() -- This read and bring all the lines into one list 
# f = open(file_path, "r", encoding = "utf")
# lines = f.readlines()
# f.close()
# print(lines)

# lines = f.readlines()
# f.close()
# print("Lines list:", [line.rstrip() for line in lines])

# Iterate over lines (memory-friendly)
# f = open(file_path, "r", encoding = "utf-8")
# for line in f:
#     print("->", line.strip())
# f.close()



# other better way to close file 

# using with open(...) as f: (which is the best practise)

# Write safely

# with open(file_path, "w", encoding ="utf-8") as f:
#     f.write("My To do List\n")
#     f.write(" - Revise Python file handling\n")
#     f.write(" - Practise error handling within a function")
#     f.write(" - Practise JSON & CSV\n")


# # Append safely

# with open(file_path, "a", encoding ="utf-8") as f:
#     f.write(" - Build a small project\n")


# from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok = True)
# workspace / "missing_flies.txt"

# # error handling
# try:
#     with open(workspace / "missing_files.txt", "r") as f:
#         content = f.read()
#         print("File content:", content)
# except FileNotFoundError:
#     print("Oops! That file doesn't exist yet.")
#     print("Let's create it first!")

#     with open(workspace / "missing_files.txt", "w") as f:
#         f.write("Now I exist!")
#     print("File created successfully!")


# checking if files exist before using them

# from pathlib import Path
# workspace = Path("workspace_files")
# file_path = workspace / "notes.txt"

# # check if our file exists
# if file_path.exists():
#     print(f"Found the file: {file_path.name}")

#     # Get some information about the file
#     file_size = file_path.stat().st_size
#     print(f"file size: {file_size} bytes") 

#     # Read and show the content
#     with open(file_path, "r", encoding ="utf-8") as f:
#         content = f.read()
#         print(f"Content preview: {content[:50]}...")
# else:
#     print(f"File{file_path.name} doesn't exist")
#     print("You might want to create it first!")

    
# Working with JSON Files

# import json
# from pathlib import Path

# workspace = Path("workspace_files")
# # Create some student data (like a mini database)
# student_data = {
#     "name": "Adeyemi",
#     "age": 22,
#     "courses":["Python", "Data Science", "Web Development"],
#     "grades":{"Python":"A", "Data Science": "B+", "Web Development": "A-"},
#     "is_graduated": False
# }

# # Save the data to a JSON file
# json_file = workspace / "student_data.json"
# with open(json_file, "w", encoding = "utf-8") as f:
#     json.dump(student_data, f, indent =2) # indent=2 makes it pretty and readable

# print("Student data saved to JSON file!")


# # Now read it back
# with open(json_file, "r", encoding = "utf-8") as f:
#     loaded_data = json.load(f)

# print("\nData read from JSON file:")
# print(f"Student name: {loaded_data['name']}")
# print(f"Age: {loaded_data['age']}")
# print(f"Courses: {', '.join(loaded_data['courses'])}")
# print(f"Python grade: {loaded_data['grades']['Python']}")



#Working with CSV files

# import csv
# from pathlib import Path

# workspace = Path("workspace_files")
# csv_file = workspace / "students.csv"

# # Create sample student data

# students = [
#     ["Name", "Age", "Course", "Grade"], # Header row
#     ["Precious", 20, "Python", "A"],
#     ["Favour", 22, "JavaScript", "B+"],
#     ["Ore", 21, "Python", "A-"],
#     ["Susan", 23, "Data Science", "A"],

# ]

# # Write data to CSV file
# with open(csv_file, "w", newline ="", encoding = "utf-8") as f:
#     writer = csv.writer(f)       
#     writer.writerows(students)        # This write all the rows at once

# print("Student data written to CSV file!")



# # Read the CSV file back

# print("\nReading CSV file:")
# with open(csv_file, "r", encoding ="utf-8") as f:
#     reader = csv.reader(f)

#     for row_number, row in enumerate(reader):
#         if row_number == 0:  #  Header row
#             print(f"Headers: {' | '.join(row)}")
#             print("-" * 40)
#         else:  # Data rows
#             name, age, course, grade = row
#             print(f"{name} ({age}  years) - {course}: {grade}")



# Working with Multiple Files at Once

# from pathlib import Path

# workspace = Path("workspace_files")
# input_file = workspace / "original.txt"
# output_file = workspace / "processed.txt"

# # Create an input file with some text
# sample_text = """ hello world
# python programming
# file handling tutorial
# learning is fun"""

# with open(input_file, "w", encoding ="utf-8") as f:
#     f.write(sample_text)

# print("Created input file")

# # Process the file: read from input, write processed version to output
# with open(input_file, "r", encoding = "utf-8") as infile, \
#      open(output_file, "w", encoding = "utf-8") as outfile:
    
#     line_number = 1
#     for line in infile:
#           # Process each line: make it uppercase and add line number
#           processed_line = f"Line {line_number}: {line.strip().upper()}\n"
#           outfile.write(processed_line)
#           line_number +=1

# print("File processing complete")

# # Show the results
# print("\nOriginal file")
# with open(input_file, "r", encoding ="utf-8") as f:
#      print(f.read())

# print("\nprocessed file")
# with open(output_file, "r", encoding = "utf-8") as f:
#      print(f.read())    



# Moving Around Inside a File 

from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "story.txt"

# Create a sample story file

story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hopp into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""


with open(file_path, "w", encoding = "utf-8") as f:
    f.write(story)


print("Created a story file!")

# Now let's explore moving around in the file

with open(file_path, "r", encoding = "utf-8") as f:
    print("\nFile positioning demo:")

    # Read first 20 characters 
    first_part = f.read(20)
    print(f"First 20 characters: '{first_part}'")

    # check where we are now
    current_position = f.tell()
    print(f"Current position in file: {current_position}")

    # Jump to the beginning
    f.seek(0)
    print(f"After seeking to beginning: position {f.tell()}")

    # Jump to position 50 and read from there
    f.seek(50)
    rest_of_line = f.readline()
    print(f"Reading from position 50: '{rest_of_line.strip()}'")

    # Go back to beginning and read the first line
    f.seek(0)
    first_line = f.readline()
    print(f"First line: '{first_line.strip()}'")