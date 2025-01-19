#Write a program in python to check whether a number is armstrong or not.
n=int(input("Enter any number: "))
p=n
sum=0
c=0
while p!=0:
   c+=1
   p//=10
p=n
while p!=0:
    r=p%10
    sum+=r**c
    p//=10
if sum==n:
    print("%d is an armstrong number."%(n))
else:
    print("%d is not an armstrong number."%(n))
