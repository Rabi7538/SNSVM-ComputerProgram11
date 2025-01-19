#Write a program in python using function to take input in a list and print it.
def list():
    l=[]
    ch='Y'
    while ch.upper()=='Y':
        p=int(input("Enter the element: "))
        l.append(p)
        ch=input("Do you want to add more (Y/N): ")
    return l
def main():
    print("The list is",list())
main()
