def Multi(a,b):
    multi=a*b
    return multi
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("Multiplication of %d and %d is %d"%(a,b,Multi(a,b)))
main()