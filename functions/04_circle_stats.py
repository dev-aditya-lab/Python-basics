import math

def circle_stats(radius):
	area = math.pi * radius ** 2
	circumference = 2 * math.pi * radius
	return area, circumference

a, c = circle_stats(3)
a = round(a, 2)
c = round(c, 2)
print("Area:", a, "Circumference:", c)
