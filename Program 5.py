#Write a program to find the division of two numbers.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if b==0:
	print("Cannot divide by zero.")
else:
	m=a/b
	print("Division of %d and %d is %d."%(a,b,m))
