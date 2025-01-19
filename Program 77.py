#Write a program in python to count and print the perfect number between certain range.
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value: "))
count=0
for i in range (m,n+1):
    p=i
    sum=0
    c=0
    for j in range (1,i//2+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,end=",")
        count+=1
print("\nTotal perfect number between %d and %d is %d."%(m,n,count))
