#Write a program in python using function to count and print the perfect number between certain range.
def perfect(n):
    sum=0
    for i in range (1,n//2+1):
        if n%i==0:
            sum+=i
    return sum
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if perfect(i)==i:
            print(i,end=",")
            count+=1
    print("\nTotal perfect number between %d and %d is %d."%(m,n,count))
main()
