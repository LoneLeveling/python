#Example: Calculating the circumference of a Circle
#Circumference of a Circle=2*pi*R
import math
radius=float(input("Enter radius of the circle: "))
circumference=2*math.pi*radius
print("Circumference of the Circle:",round(circumference,2)) #round() rounds the decimal part till 2 digits


#Area of a Circle
radius1=float(input("Enter radius of the circle: "))
area=math.pi*radius1**2
print(f"Area of the circle: {round(area,2)}")


#Calculating the Hypotenuse of a Right Angled Triangle
base=float(input("Enter the base value of the Triangle: "))
perpendicular=float(input("Enter the perpendicular value of the Triangle: "))
hypotenuse=math.sqrt(base**2+perpendicular**2)

#Another way to write above: hypotenuse=math.sqrt(pow(base,2)+pow(perpendicular,2))

print(f"Hypotenuse of the Triangle: {round(hypotenuse,2)}")