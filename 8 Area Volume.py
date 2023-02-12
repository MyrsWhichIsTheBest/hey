import math


def area_finder(radius):
    return 4*math.pi*radius**2


def volume_finder(radius):
    return 4/3*math.pi*radius**3


number = int(input("Number"))
print(area_finder(number))
print(volume_finder(number))
