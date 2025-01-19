#Write a program in python using function to check whether a number is magic or not.
def magic(n):
    p=n
    sum=0
    x=0
    while p!=0:
        r=p%10
        sum+=r
        p//=10
    a=sum
    while a!=0:
        y=a%10
        x=x*10+y
        a//=10
    m=sum*x
    return m
def main():
    n=int(input("Enter the number: "))
    if magic(n)==n:
        print(n,"is a magic number.")
    else:
        print(n,"is not a magic number.")
main()
