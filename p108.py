def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)
def main():
    a=int(input("Enter any number:"))
    b=int(input("Enter any number:"))
    print("A=",a)
    print("B=",b)
    a,b=swap(a,b)
    print("After swapping")
    print("A=",a)
    print("B=",b)
main()