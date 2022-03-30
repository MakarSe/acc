import math
h1 = float(input("Enter height: "))
r1 = float(input("Enter radius of cylinder: "))

def Volume (h,r):
    return (math.pi * r * r * h)

print(Volume(h1 , r1))