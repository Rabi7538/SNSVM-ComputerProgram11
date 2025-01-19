#Write a program in python to check whether a number is neon or not.
n=int(input("Enter any number: "))
p=n*n
sum=0
while p!=0:
    r=p%10
    sum+=r
    p//=10
if sum==n:
    print("%d is a neon number."%(n))
else:
    print("%d is not a neon number."%(n))
