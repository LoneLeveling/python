# logical operators = used on conditional statements

#  and = checks two or more conditions are True
#  or = checks if at least one condition is True
#  not = True if condition is False, and vice versa

temp=-11
if temp>=10 and temp<30:
    print("The temperature is good")
else:
    print("The temperature is bad")

if temp<=0 or temp>=30:
    print("The temperature is bad")
else:
    print("The temperature is good")

sunny=True
if not sunny:
    print("It is sunny outside")
else:
    print("It is cloudy outside")