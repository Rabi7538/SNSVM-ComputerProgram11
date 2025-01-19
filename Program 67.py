#Write a program in python to check whether a number is palindrome or not.
n=int(input("Enter any number: "))
p=n
sum=0
while p!=0:
    s=p%10
    sum=sum*10+s
    p//=10
if sum==n:
    print("%d is a palindrome number."%(n))
else:
    print("%d is not a palindrome number."%(n))
