#Shopping Cart Example
from functools import total_ordering

item=input("Enter the Item you would like to buy: ")
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity of the item you would like to buy: "))

total_ordering =price*quantity

print(f"You have bought {quantity} * {item}/s")
print(f"The total order amount is ₹{total_ordering}")