#Write a program in python to find the factorial of a number.
num=int(input("Enter any number: "))
fact=1
for i in range (1,num+1):
    fact*=i
print("Factorial of %d is %d."%(num,fact))