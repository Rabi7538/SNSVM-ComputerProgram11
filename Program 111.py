#Write a program in python using fucnion to find the sum of two numbers.
#Method2: Function with argument but not returning value.
def Add(a,b):
    sum=a+b
    print("Addition of %d and %d is %d."%(a,b,sum))
def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    Add(a,b)
main()
