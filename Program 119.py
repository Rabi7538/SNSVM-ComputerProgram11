#Write a program in python using function to swap two mumbers using third variable.
def swap(m,n):
    print("Before swapping")
    print("M =",m)
    print("N =",n)
    temp=m
    m=n
    n=temp
    print("After swapping")
    print("M =",m)
    print("N =",n)
def main():
    m=int(input("Enter the first number: "))
    n=int(input("Enter the second number: "))
    swap(m,n)
main()
