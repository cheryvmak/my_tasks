empty_list = []
print(empty_list)

empty_list2 = list()
print(empty_list2)

numbers = [1, 2, 3, 4, 5]
print(numbers)


fruits =["apple", "banana", "chery"]
print(fruits)

mixed_list =["Alice", 25, 5.8, True]
print(mixed_list)

chars = list("hello")
print(chars)


my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

numbers_range = list(range(5))
print(numbers_range)

# Squares of numbers 0–4
squares = [x**2 for x in range(5)]
print(squares)

# Even numbers between 0–10
evens = [x for x in range(11) if x % 2 ==0]
print(evens)


matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)

print(matrix[0])
print(matrix[0][1])


fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])

items = ["rice", "beans", "yam", "rice"]
print(items)


numbers = [1, 2, 3]
numbers[1] = 20
print(numbers)


mixed = [10, "Nigeria", 3.14, True]
print(mixed)


nested_list = [[1, 2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])


names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)