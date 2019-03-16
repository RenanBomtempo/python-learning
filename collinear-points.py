import math

#--get three points--
#get first point
print("First point:")
x1 = float(input("x = "))
y1 = float(input("y = "))

#get second point
print("\nSecond point:")
x2 = float(input("x = "))
y2 = float(input("y = "))

#get third point
print("\nThird point:")
x3 = float(input("x = "))
y3 = float(input("y = "))

#calculate slopes
slope1 = math.fabs((y1 - y2)/(x1 - x2))
slope2 = math.fabs((y1 - y3)/(x1 - x3))

#check if slopes are the same
if slope1 == slope2:
    print("\nYES! The points are collinear.")
    exit()
else:
    print("\nNO! The points are not collinear.")

#check what type of triangle they form
side1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
side2 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
side3 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)

print(side1)
print(side2)
print(side3)

if side1 == side2:
    if side1 == side3:
        print("The points form an Equilateral triangle")
    else: 
        print("The points form an Isoceles triangle")   
elif side1 == side3 or side2 == side3:
    print("The points form an Isoceles triangle")   
else:
    print("The points form an Scalene triangle")   