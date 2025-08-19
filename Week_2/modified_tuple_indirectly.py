
# Task 5

shopping_list = []
shopping_item_1 = (input("Enter shopping item 1: "))
shopping_item_2 = (input("Enter shopping item 2: "))
shopping_item_3 = (input("Enter shopping item 3: "))
print(shopping_list.append(shopping_item_1))
print(shopping_list.append(shopping_item_2))
print(shopping_list.append(shopping_item_3))
print(shopping_list)
my_shopping_list = tuple(shopping_list)
print(my_shopping_list)
new_shopping_list = (list(my_shopping_list))
print(new_shopping_list)
new_item_1 = input("Enter additional item 1: ")
new_item_2 = input("Enter additional item 2: ")
new_shopping_list.append(new_item_1)
new_shopping_list.append(new_item_2)
print(new_shopping_list)
updated_shopping_list = tuple(new_shopping_list)
print(updated_shopping_list)
print("|".join(updated_shopping_list))