#Topic: if() statements in Python
# if = Do some code only if some condition is True, else do something else

age=int(input("Enter your age: "))
if age >= 25:
    print("You are old enough to drink 🥤 coffee 🙈")
elif age<0:
    print("You haven't been born yet 🤰")
else:
    print("You better drink milk kiddo 💁")



#Example 2:
response=input("Would you like to have food ? (Y/N): ")
if response=="Y":
    print("Then just eat the milk pudding kid")
elif response=="N":
    print("If not hungry then just study kid")
else:
    print("Enter a valid response")


#Example 3:
name=input("Enter your name: ")
if name=="":
    print("Your name is empty 😡, enter your name for me to capitalize it")
else:
    print(f"Your name in capitals is: {name.upper()} ☺️")


#Example 4:
for_sale=True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")