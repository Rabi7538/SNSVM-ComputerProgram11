#Write a program in python to take input in a list and print it.
#Method 1
l=[]
n=int(input("How many elements you want to enter: "))
for i in range (n):
    p=int(input("Enter the %d element: "%(i+1)))
    l.append(p)
print("The list is",l)
