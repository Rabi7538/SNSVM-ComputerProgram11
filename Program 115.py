#Write a program in python using fucnion to find the multiplication of two numbers.
def multiply(a,b):
    multiply=a*b
    return multiply
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("Multiplication of %d and %d is %d."%(a,b,multiply(a,b)))
main()
