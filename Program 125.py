#Write a program in python using function to find the prime number between certain range.
def prime(n):
    c=0
    for i in range (1,n//2+1):
        if n%i==0:
            c+=1
        if c==2:
            return False
    return True
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        if prime(i)==True:
            print(i, end=",")
            count+=1
    print("\nTotal prime numbers between %d and %d is %d."%(m,n,count))
main()
