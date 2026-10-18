#Python Calculator

operator=input("Enter the operator: (+ - * /): ")
if operator=="+":
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print(round(num1+num2,2))
elif operator=="-":
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print(round(num1-num2,2))
elif operator=="*":
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print(round(num1*num2,2))
elif operator=="/":
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print(round(num1/num2),2)
else:
    print("Input a valid operator")
