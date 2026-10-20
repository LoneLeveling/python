# Python weight Calculator

weight=float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (K OR L):")
if unit=="k" or unit=="K":
    weight=weight*2.205
    unit="Lbs."
    print(f'Your weight is {round(weight, 2)} {unit} pounds')
elif unit=="l" or unit=="L":
    weight=weight/2.205
    unit="kgs"
    print(f'Your weight is {round(weight, 2)} {unit} pounds')
else:
    print(f"Sorry, your input \"{unit}\" is not valid input")
    # print(f'Sorry, your input "{unit}" is not valid')

