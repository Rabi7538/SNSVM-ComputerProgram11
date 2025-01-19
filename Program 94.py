#Write a program in python to take input in a list and search the element using linear search tehnique.
l=[]
while True:
    p=int(input("Enter the element: "))
    l.append(p)
    ch=input("Do you want to add more(Y/N): ")
    if ch.upper()=='Y':
        continue
    else:
        break
print("The list is",l)
search=int(input("Enter the element you want to search: "))
flag=False
for i in range (len(l)):
    if l[i]==search:
        flag=True
        pos=i+1
        break
if flag==True:
    print("The searched element %d is found in %d position."%(search,pos))
else:
    print("The searched element %d is not found."%(search))
