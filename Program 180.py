#Write a program in python using function to check whether a number is special or not.
def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
def special(n):
    p=n
    sum=0
    while p!=0:
        r=p%10
        sum+=factorial(r)
        p//=10
    return sum
def main():
    n=int(input("Enter the number: "))
    if n==special(n):
        print(n,"is a special number.")
    else:
        print(n,"is not a special number.")
main()
