
''' **Task1: Your Favorite Life Quote**
- Ask the user to input their favorite quote.

- Convert it to title case.

- Print it with quotation marks using escape sequences. '''


# Task 1
fav_quote = input("Enter your favorite quote: ")
my_fav_quote = fav_quote.title()
print("\"" + my_fav_quote + "\"")



''' **Task 2: Shopping List Manager**
- Create an empty list.

- Ask the user to enter 3 shopping items (one by one).

- Add them to the list.

- Display the list as a single string, separated by commas. '''



# Task 2
shopping_list = []
shopping_item_1 = (input("Enter shopping item: "))
shopping_item_2 = (input("Enter shopping item: "))
shopping_item_3 = (input("Enter shopping item: "))
print(shopping_list.append(shopping_item_1))
print(shopping_list.append(shopping_item_2))
print(shopping_list.append(shopping_item_3))
print(shopping_list)




''' **Task 3: Word Counter**
- Ask the user for a sentence.

- Split the sentence into a list of words.

- Print how many words are in the sentence. '''


# Task 3

sentence = input("Enter a sentence: ")
split_word = sentence.split()
print(len(split_word))




''' **Task 4: Name Organizer**
- Ask the user to enter 5 names (separated by spaces).

- Convert all names to lowercase.

- Sort the list alphabetically.

- Display them one name per line.
  -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` '''


# Task 4

names = input("Enter 5 names separated by spaces: ").lower()
all_names = names.split()
all_names.sort()
print(all_names)
for name in range(len(all_names)):
    print(all_names[name])
    



''' **Task 5: Student Score Tracker**

- Ask the user for 3 student names.

- For each student, ask for their score.

- Store the results in two lists (one for names, one for scores).

- Print a formatted output showing Name — Score, aligned neatly.
  - Tips: You are to start by creating two empty lists. '''


# Task 5

student_name = []
student_score =[]

student_name_1 = input("Enter the name of the first student: ")
student_name_2 = input("Enter the name of the second student: ")
student_name_3 = input("Enter the name of the third student: ")

student_score_1 = input(f"Enter {student_name_1} score: ")
student_score_2 = input(f"Enter {student_name_2} score: ")
student_score_3 = input(f"Enter {student_name_3} score: ")


student_name.append(student_name_1)
student_name.append(student_name_2)
student_name.append(student_name_3)


student_score.append(student_score_1)
student_score.append(student_score_2)
student_score.append(student_score_3)

print(f"{student_name[0]} \t—\t{student_score[0]}")
print(f"{student_name[1]} \t—\t{student_score[1]}")
print(f"{student_name[2]} \t—\t{student_score[2]}")


''' **Task 6: Word Analyzer**
- Ask the user to input a word.

- Print the length of the word.

- Check if it is all uppercase, all lowercase, or title case.

- Reverse the word using slicing.'''


# Task 6

end_user =  input("Enter a word: ")
print(len(end_user))
in_upper_case  =  end_user.isupper()
print(f"The word entered is in upper_case: {in_upper_case}")
in_lower_case  =  end_user.islower()
print(f"The word entered is in lower_case: {in_lower_case}")
in_title_case  =  end_user.istitle()
print(f"The word entered is in title_case: {in_title_case}")
print(end_user[::-1])




''' **Task 7: List Manipulation**
- Create a list of five cities.

- Replace the third city with a new one (entered by the user).

- Remove the last city.

- Add a new city to the beginning of the list.

- Print the updated list. '''


# Task 7

cities = ["Abeokuta", "Ibadan", "Uyo", "Portharcourt", " Benin"]
print(cities)
cities[2] = input("Enter a new city to replace the third city: ")
print(cities)
remove_list_city = cities[0:4]
print(remove_list_city)
updated_city_list = remove_list_city
updated_city_list.insert(0, "Lagos")
print(updated_city_list)

