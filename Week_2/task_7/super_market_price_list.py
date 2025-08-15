# Task 2

items = ["pencil", "dettol","batteries","shoe","detergent"]

user_price_1 = float(input("price of the first item: "))
user_price_2 = float(input("price of the second item: "))
user_price_3 = float(input("price of the third item: "))
user_price_4 = float(input("price of the fourth item: "))
user_price_5 = float(input("price of the fifth item: "))

user_prices = [user_price_1, user_price_2, user_price_3, user_price_4, user_price_5]

super_market_p_list = {}

super_market_p_list["items"] = items
super_market_p_list["user_prices"] = user_prices
print(super_market_p_list)

print("Enter the updated price ")
new_user_price_1 = float(input("updated price of the first item: "))
new_user_price_2 = float(input("updated price of the second item: "))
new_user_price_3 = float(input("updated price of the third item: "))
new_user_price_4 = float(input("updated price of the fourth item: "))
new_user_price_5 = float(input("updated price of the fifth item: "))


updated_prices = [new_user_price_1, new_user_price_2, new_user_price_3, new_user_price_4, new_user_price_5]

super_market_p_list.update({"user_price": updated_prices})
print(super_market_p_list)