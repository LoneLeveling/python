# Typecasting = The process of converting a value of one data type to another(string, integer, float, boolean)
#2 Types: Explicit Vs Implicit
#Explicit: Manually converting the variable data type into another
#Implicit: When a value/variable converted into another data type automatically.


#Explicit Type Casting
name="Abhi"
age=26
height=6.11
meal_taken=False
print(type(name)) #type() function return the type of the variable
print(type(age))
print(type(height))
print(type(meal_taken))

print("---------------------------")

#Typecasting str to boolean
name=bool(name)
print(type(name))
print(name)
#Above prints Ture bcz name is not empty str, if we have name="", then the bool(name)=False
#But why would we want to convert a str to bool?
#Imagine if we ask user to input their name and if they didn't we want to print "name not entered", so we can write a logic like below just because we are able to convert a str to bool type
userName=""
userName=bool(userName) #Even if we do not write this line still the logic would work
if userName:
 print("name entered")
else:
 print("name not entered")
# NOTE:bool() converts a value based on whether it is truthy or falsy. A non-empty string is truthy, so bool("Abhi") returns True.


# Typecasting int 'age' to float
age=float(age)
print(type(age))

# Typecasting float 'height' to 'int'
height=int(height)
print(type(height))
print(height)

#Typecasting boolean to str
meal_taken=str(meal_taken)
print(type(meal_taken))

#Implicit Type Casting
x=2
y=2.0
x=x/y
print(x)