#Write a program in python using fucnion to find the sum of two numbers.
#Method1: Function with argument and returning value.
def Add(a,b):
    sum=a+b
    return sum
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    s=Add(a,b)
    print("Addition of %d and %d is %d."%(a,b,s))
main()
