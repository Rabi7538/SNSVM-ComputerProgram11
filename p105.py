def Div(a,b):
    div=a/b
    return div
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if b==0:
        print("Not divisible by zero")
    else:
        print("Division of %d and %d is %d"%(a,b,Div(a,b)))

main()