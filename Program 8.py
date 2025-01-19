#Write a program in python to swap two numbers using third variable.
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
print("Before swapping")
print("M=",m)
print("N=",n)
temp=m
m=n
n=temp
print("After swapping")
print("M=",m)
print("N=",n)