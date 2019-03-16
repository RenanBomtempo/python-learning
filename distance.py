import math

#get first point
print("First point:")
print("x = ", end='')
x1 = float(input())
print("y = ", end='')
y1 = float(input())

#get second point
print("\nSecond point:")
print("x = ", end='')
x2 = float(input())
print("y = ", end='')
y2 = float(input())

#calculate distance
distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("\nThe distance between the two points is: ", distance)