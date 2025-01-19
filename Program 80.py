#Write a program in python to count and print the automorphic number between certain range.
import math
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value: "))
count=0
for i in range (m,n+1):
    p=i
    c=0
    while p!=0:
        c+=1
        p//=10
    p=i*i
    q=p%math.pow(10,c)
    if q==i:
        print(i,end=",")
        count+=1
print("\nTotal automorphic number between %d and %d is %d."%(m,n,count))
