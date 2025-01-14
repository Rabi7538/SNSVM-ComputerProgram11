def Add(a,b):
    sum=a+b
    return sum
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("Addition of %d and %d is %d"%(a,b,Add(a,b)))
main()