#Write a program in python to check whether a number is automorphic or not.
import math
n=int(input("Enter any number: "))
p=n
count=0
while p!=0:
    count+=1
    p//=10
p=n*n
q=p%math.pow(10,count)
if q==n:
    print("%d is an automorphic number."%(n))
else:
    print("%d is not an automorphic number."%(n))
