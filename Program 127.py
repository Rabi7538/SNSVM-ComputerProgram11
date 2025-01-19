#Write a program in python using function to print the fibonacci series.
def fib(n):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range (3,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
def main():
    n=int(input("Enter the number of terms: "))
    fib(n)
main()
