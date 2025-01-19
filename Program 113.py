#Write a program in python using fucnion to find the sum of two numbers.
#Method4: Function with no argument and no returning value.
def Add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sum=a+b
    print("Addition of %d and %d is %d."%(a,b,sum))
def main():
    Add()
main()
