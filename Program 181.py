#Write a program in python using function to check whether a number is neon or not.
def neon(n):
    p=n*n
    sum=0
    while p!=0:
        r=p%10
        sum+=r
        p//=10
    return sum
def main():
    n=int(input("Enter the number: "))
    if n==neon(n):
        print("%d is a neon number."%(n))
    else:
        print("%d is not a neon number."%(n))
main()
