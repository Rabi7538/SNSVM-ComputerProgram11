#Write a program in python using fucnion to find the subtraction of two numbers.
def subtract(a,b):
    sub=a-b
    return sub
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("Subtraction of %d and %d is %d."%(a,b,subtract(a,b)))
main()
