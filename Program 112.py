#Write a program in python using fucnion to find the sum of two numbers.
#Method3: Function with no argument but returning value.
def Add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sum=a+b
    return a,b,sum
def main():
    a,b,s=Add()
    print("Addition of %d and %d is %d."%(a,b,s))
main()
