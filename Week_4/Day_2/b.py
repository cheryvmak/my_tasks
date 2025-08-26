

def greet(name):
    return f"Hello, {name}! I am creating my own module"

def reverse_string(string):
    return string[::-1]

def count_characters(string):
    return len(string)

def count_words(string):
    return len(string.split())

def count_sentences(string):
    return len(string.split("."))


print(greet("Ade"))
print(reverse_string("house"))
print(count_characters("level"))
print(count_words("They are both coding"))
print(count_sentences("They are both coding. The boy is enjoying it"))