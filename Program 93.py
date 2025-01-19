#Write a program in python to take input in a list and print it.
#Method 3
l=[]
ch='Y'
while ch.upper()=='Y':
    p=int(input("Enter the element: "))
    l.append(p)
    ch=input("Do you want to add more (Y/N): ")
print("The list is",l)
