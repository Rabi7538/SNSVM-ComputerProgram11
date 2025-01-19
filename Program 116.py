#Write a program in python using fucnion to find the division of two numbers.
def divide(a,b):
    div=a/b
    return div
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if b==0:
        print("Cannot divide by zero.")
    else:
        print("Division of %d and %d is %d."%(a,b,divide(a,b)))
main()
