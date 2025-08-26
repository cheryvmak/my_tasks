
import a
import b

# lets use the functions in the a.py file
print("")
print("=== Math Functions ==")
print("5 + 3 + 7 =", a.add(5, 3, 7))
print("10 - 4 - 3 =", a.subtract(10, 4, 3))
print("6 * 7  * 1=", a.multiply(6, 7, 1))
print("20 / 5 / 2", a.divide(20, 5, 2))

# lets use the functions in the b.py file
print("")
my_rhyme = """
Black, black, black,
The color of the night.
Stars come out,
And the moon shines bright. 

Black, black, black,
The color of a shoe. 
Paint it nice,
It looks brand new!

Black, black, black,
The color of a cat. 
Soft and quick,
What do you think of that?
"""

print("My name is Micheal Scoffield. My code message is: ",b.reverse_string(my_rhyme))
print("The total number of characters in my message is: ", b.count_characters(my_rhyme))
print("The total number of words in my message is: ", b.count_words(my_rhyme))
print("The total number of sentences im my message is: ", b.count_sentences(my_rhyme))