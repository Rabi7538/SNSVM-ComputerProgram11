#Write a program in python using function to check whether a number is palindrome or not.
def palindrome(n):
    p=n
    sum=0
    while p!=0:
        s=p%10
        sum=sum*10+s
        p//=10
    return sum
def main():
    n=int(input("Enter any number: "))
    if n==palindrome(n):
        print("%d is a palindrome number."%(n))
    else:
        print("%d is not a palindrome number."%(n))
main()
