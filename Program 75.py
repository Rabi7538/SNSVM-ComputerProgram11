#Write a program in python to count and print the palindrome number between certain range.
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value: "))
count=0
for i in range (m,n+1):
    p=i
    sum=0
    while p!=0:
        s=p%10
        sum=sum*10+s
        p//=10
    if sum==i:
        print(i,end=",")
        count+=1
print("\nTotal palindrome number between %d and %d is %d."%(m,n,count))