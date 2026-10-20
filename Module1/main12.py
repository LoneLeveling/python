#Python Temperature Conversion Program

temp=float(input("Enter the temperature in Celsius or Fahrenheit: "))
unit=input(("Is the temperature in Celsius or Fahrenheit? Enter C or F:"))
if unit=="C" or unit=="c":
    temp=(9*temp)/5+32
    print(f"The temperature in Fahrenheit is {round(temp,2)} Fahrenheit")
elif unit=="F" or unit=="f":
    temp=(temp-32)*5/9
    print(f"The temperature in Celsius is {round(temp,2)} Celsius")
else:
    print(f'"{unit}" is an invalid temperature unit, Please enter a valid input')

