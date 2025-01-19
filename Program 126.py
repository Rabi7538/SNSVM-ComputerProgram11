#Write a program in python using function to find the factorial of a number.
def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
def main():
    n=int(input("Enter the number: "))
    f=factorial(n)
    print("Factorial of %d is %d."%(n,f))
main()
