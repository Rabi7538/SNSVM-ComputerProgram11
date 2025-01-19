#Write a program in python using function to count and print the automorphic number between certain range.
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
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if automorphic(i)==i:
            print(i,end=",")
            count+=1
    print("\nTotal automorphic number between %d and %d is %d."%(m,n,count))
main()
