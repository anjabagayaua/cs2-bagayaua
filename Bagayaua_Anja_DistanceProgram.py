import math

x1= float (input("Enter x1: "))
x2= float (input("Enter x2: "))
y1= float (input("Enter y1: "))
y2= float (input("Enter y2: "))

distance= math.sqrt(pow(x2-x1,2)+ pow(y2-y1,2))

print ("Distance is", distance)

#Reflection
#The math library helped simplify this program by introducing the square root (sqrt) instead of manually findingg the square root it or adding other commands to find it.
#The library let me use the functions freely, like sqrt and pow.
#The program would be a lot harder becaus I would have to add more functions to get to the same result.