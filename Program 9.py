#Write a program in python to swap two numbers without using third variable.
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
print ("Before swapping")
print("M=",m)
print("N=",n)
m=m+n
n=m-n
m=m-n
print ("After swapping")
print("M=",m)
print("N=",n)