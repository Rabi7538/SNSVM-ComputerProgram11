def add(a,b):
    add=a+b
    return add
def sub(a,b):
    sub=a-b
    return sub
def multi(a,b):
    multi=a*b
    return multi
def div(a,b):
    div=a/b
    return div
def prop():
    print("""Menu of the program
1.Addition
2.Subtraction
3.Multiplication
4.Division""")
    ch=int(input("Enter your choice:"))
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if ch==1:
        print("Addition of %d and %d is %d"%(a,b,add(a,b)))
    elif ch==2:
        print("Subtraction of %d and %d is %d"%(a,b,sub(a,b)))
    elif ch==3:
        print("Multiplication of %d and %d is %d"%(a,b,multi(a,b)))
    elif ch==4:
        if b==0:
            print("Cannot divisible by zero")
        else:
            print("Division of %d and %d is %d"%(a,b,div(a,b)))
    else:
        print("Worng choice")
prop()