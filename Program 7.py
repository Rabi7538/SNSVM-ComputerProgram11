#Write a program in python to find the roots of a quadratic equation
import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant value: "))
if a==0:
	print("This is not a quadratic equation.")
else:
	d=b*b-4*a*c
	if d<0:
		print("Roots are imaginary.")
	elif d==0:
		x=-b/(2*a)
		print("Roots of the equation is",x)
	else:
		x1=-b+math.sqrt(d)/(2*a)
		x2=-b-math.sqrt(d)/(2*a)
		print("Roots of the equation are",x1,x2)