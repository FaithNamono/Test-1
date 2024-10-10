import math


#Using a function create a program that calculates the volume of a cylinder
radius = int(input("enter the radius of the cylinder"))
height = int(input("enter the height if the cylinder"))
pie = math.pi
volume = pie * radius **2 * height
print(f"the volume of the cylinder is {int(volume)}")