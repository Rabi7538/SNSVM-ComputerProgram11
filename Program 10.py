#Write a program in python to find the addition, subtraction, multiplication and division using menu driven technique.
print('''Menu of the Program
1. Addition
2. Subtraction
3. Multiplication
4. Division''')
n=int(input("Enter your choice: "))
a=int(input("Enter the first number: "))
b=int(input("Enter thr second number: "))
if n==2:
    print("Subtraction of %d and %d is %d."%(a,b,a-b))
elif n==1:
    print("Addition of %d and %d is %d."%(a,b,a+b))
elif n==3:
    print("Multiplication of %d and %d is %d."%(a,b,a*b))
elif n==4:
    if b==0:
        print("Cannot divide by zero.")
    else:
        print("Division of %d by %d is %d."%(a,b,a/b))
else:
    print("Wrong Choice!")
