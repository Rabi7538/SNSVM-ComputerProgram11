#Write a program in python to count and print the armstrong number between certain range.
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value: "))
count=0
for i in range (m,n+1):
    p=i
    sum=0
    c=0
    while p!=0:
        p//=10
        c+=1
    p=i
    while p!=0:
        r=p%10
        sum+=r**c
        p//=10
    if sum==i:
        print(i,end=",")
        count+=1
print("\nTotal armstrong number between %d and %d is %d."%(m,n,count))
