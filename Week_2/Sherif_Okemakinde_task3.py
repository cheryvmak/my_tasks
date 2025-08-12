# Task1

'''
1. Write a program to take a string input from the user and display it in uppercase.

2. Given the string "python", print its first and last characters.

3. Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.

4. Write a program to count the number of characters in a string without using len().

5. Given "Hello World", replace "World" with "Python".'''


# Task1

# Q1.
client_name = input("Enter your name: ")
print(client_name.upper())

# Q2.

text = "python"
print(text[0:6:5])

#Q3.

name = input("Enter your name: ")
print(f"Hello, {name}")

#Q4.

word = "Thank you my brother"
print(word.index("brother"))

#Q5.

a = "Hello World"
a.replace("World", "python")
print(a)



# Task2

'''

6. Check if a given string contains the substring "python" (case-insensitive).

7. Write a program to reverse a string without using slicing ([::-1]).

8. Given a string with extra spaces, remove the leading and trailing spaces.

9. Ask the user to enter a sentence and print the number of vowels in it.

10. Convert a string "1234" to an integer and multiply it by 2. '''


# Q6.

word = "I'm enjoying coding"
print("coding" in word)

# Q7

a = "Hello"
print(a[::-1])
print(a[-1:-6:-1])


# Q8

name = "    Adeola "
print(name.strip())

# Q9

clients = input("Enter a sentence: ")
#vowels = ("aeiouAEIOU")
a = clients.count("a")
e = clients.count("e")
i = clients.count("i")
o = clients.count("o")
u = clients.count("u")
A = clients.count("A")
E = clients.count("E")
I = clients.count("I")
O = clients.count("O")
U = clients.count("U")
sum_vowel = a+e+i+o+u+A+E+I+O+U
print(f"The number of vowel in it: {sum_vowel}")

# Q10

a = "1234"
b = (int(a) * 2)
print(b)



'''Task3: Pattern Matching & Splitting**
11. Given "apple,banana,orange", split the string into a list of fruits.

12. Ask the user for a sentence and print each word on a new line.

13. Replace all spaces in a string with underscores (_).

14. Count how many times the letter "a" appears in "Banana".

15. Check if a given string starts with "https://". '''

#Q11

fruits = ("apple,banana,orange")
fruit_list = fruits.split(",")
print(fruit_list)

#Q12

user = input("Enter a sentence: ")
each_word = user.split()
print("\n".join(each_word))

#Q13

a = "he ll o"
print(a.replace(" ", "_"))


#Q14

fruit = "Banana"
a = fruit.count("a")
print(f"The letter appears: {a} times.")

#Q15

address = "https://www.goal.com"
print(address.startswith("https://"))
