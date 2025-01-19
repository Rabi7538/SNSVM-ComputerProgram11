#Write a program in python to take input in a list and print it.
#Method 2
l=[]
while True:
    p=int(input("Enter the element: "))
    l.append(p)
    ch=input("Do you want to add more (Y/N): ")
    if ch.upper()=='Y':
        continue
    else:
        break
print("The list is",l)
