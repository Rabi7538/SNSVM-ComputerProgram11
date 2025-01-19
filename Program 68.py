#Write a program in python to check whether a number is perfect or not.
n=int(input("Enter any number: "))
sum=0
for i in range (1,n//2+1):
    if n%i==0:
        sum+=i
if sum==n:
    print("%d is a perfect number."%(n))
else:
    print("%d is not a perfect number."%(n))
