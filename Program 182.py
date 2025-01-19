#Write a program in python using function to check whether a number is automorphic or not.
import math
def automorphic(n):
    p=n
    count=0
    while p!=0:
        count+=1
        p//=10
    p=n*n
    q=p%math.pow(10,count)
    return q
def main():
    n=int(input("Enter the number: "))
    if n==automorphic(n):
        print("%d is an automorphic number."%(n))
    else:
        print("%d is not an automorphic number."%(n))
main()
