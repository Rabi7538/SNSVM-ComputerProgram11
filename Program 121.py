#Write a program in python using function to find the addition, subtraction, multiplication and division using menu driven technique.
def add(a,b):
    sum=a+b
    return sum
def subtract(a,b):
    sub=a-b
    return sub
def multiply(a,b):
    mul=a*b
    return mul
def divide(a,b):
    div=a/b
    return div
def main():
    print('''Menu of the Program
1. Addition
2. Subtraction
3. Multiplication
4. Division''')
    n=int(input("Enter your choice: "))
    a=int(input("Enter the first number: "))
    b=int(input("Enter thr second number: "))
    if n==2:
        print("Subtraction of %d and %d is %d."%(a,b,subtract(a,b)))
    elif n==1:
        print("Addition of %d and %d is %d."%(a,b,add(a,b)))
    elif n==3:
        print("Multiplication of %d and %d is %d."%(a,b,multiply(a,b)))
    elif n==4:
        if b==0:
            print("Cannot divide by zero.")
        else:
            print("Division of %d by %d is %d."%(a,b,divide(a,b)))
    else:
        print("Wrong Choice!")
main()
