#Write a program in python using function to swap two mumbers without using third variable.
def swap(m,n):
    print ("Before swapping")
    print("M =",m)
    print("N =",n)
    m=m+n
    n=m-n
    m=m-n
    print ("After swapping")
    print("M =",m)
    print("N =",n)
def main():
    m=int(input("Enter the first number: "))
    n=int(input("Enter the second number: "))
    swap(m,n)
main()
