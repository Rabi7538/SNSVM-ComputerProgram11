#Write a program in python using function to check whether a number is perfect or not.
def perfect(n):
    sum=0
    for i in range (1,n//2+1):
        if n%i==0:
            sum+=i
    return sum
def main():
    n=int(input("Enter the number: "))
    if perfect(n)==n:
        print("%d is a perfect number."%(n))
    else:
        print("%d is not a perfect number."%(n))
main()
