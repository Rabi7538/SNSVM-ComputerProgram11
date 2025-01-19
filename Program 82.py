#Write a program in python to check and print the magic number between certain range.
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value:" ))
count=0
for i in range (m,n+1):
    p=i
    sum=0
    x=0
    while p!=0:
        r=p%10
        sum+=r
        p//=10
    a=sum
    while a!=0:
        y=a%10
        x=x*10+y
        a//=10
    f=sum*x
    if f==i:
        print(i,end=",")
        count+=1
print("\nTotal magic number between %d and %d is %d."%(m,n,count))
