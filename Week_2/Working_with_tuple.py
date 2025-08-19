fruits = ("apple", "banana", "cherry")
print(fruits)

numbers = 1, 2, 3
print(numbers)

single_item = ("apple",)
print(single_item)
print(type(single_item))

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


colors = ("red", "green", "blue")
print(colors[0])

# colors[1] = "yellow"  # Type Error due to its immutable character

numbers = (1, 2, 2, 3)
print(numbers)

mixed = ("apple", 3, True, 5.6)
print(mixed)

nested = (("a", "b"), (1, 2))
print(nested)


fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

print(fruits[0:2])
print(fruits[::-1])

tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

nums = (1, 2)
print(nums * 3)


fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

for fruit in fruits:
    print(fruit)           


numbers = (1, 2, 2, 2, 3, 4, 3)
print(numbers.count(2))      # count occurence of 2     
print(numbers.index(3))      # position of first occurence of 3

t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) 

t = tuple(lst)
print(t)

nums = (4, 1, 7, 3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))