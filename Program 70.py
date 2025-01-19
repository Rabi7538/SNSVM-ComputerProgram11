#Write a program in python to check whether a number is special or not.
n=int(input("Enter the number: "))
p=n
sum=0
while p!=0:
    r=p%10
    fact=1
    for i in range (1,r+1):
        fact*=i
    sum+=fact
    p//=10
if sum==n:
    print("%d is a special number."%(n))
else:
    print("%d is not a special number."%(n))
