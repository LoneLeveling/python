#Topic: String methods in python

name=input("Enter your full name:")
result=len(name) #len() method return the length of the string
print(result)

result=name.find("h") #find(): return the 1st occurrence of a character
print(result)

#To find the last occurrence we use 'rfind', r-> reverse
result=name.rfind("a")
print(result)

#capitalize(): To Capitalize 1st character of the String
name=name.capitalize()
print(name)

#upper(): To capitalize all the character of the string
print(name.upper())

#lower(): To convert all string characters to lowercase
print(name.lower())

#isdigit() : return True iff a string only contains digits 'False' otherwise.
print(name.isdigit())

#isalpha() : returns 'True' iff a string contains only alphabets, 'False' otherwise.
print(name.isalpha()) #returns 'False' even if a space character is present.

#count() : returns the no. of occurrence's of the argument passed in a given string
phone_number=input("Enter your phone number: #")
print(phone_number.count("-"))

#replace(arg1, arg2): replaces occurrences of arg1 by arg2
phone_number=phone_number.replace("-","")
print(phone_number)

#Validate user input Exercise:
# 1. userName is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

userName=input("Enter your user name:")
if not userName: #NOTE:An empty string ("") is falsy, so not userName is True.
    print("Please enter a non-empty user name")
elif len(userName)>12:
    print("username is too long")
elif userName.count(" ")>=1:#meaning username is <=12 and now we check next condition
    print("username cannot contain spaces")
elif any(char.isdigit() for char in userName): #NOTE: we used any() here which checks if a number is present in string or not, Imp NOTE: userName.isdigit() checks whether the entire string consists of digits, so it returns False for something like "Abhi123".
    print("username cannot contain digits")
else:
    print(f' "{userName}" is valid')