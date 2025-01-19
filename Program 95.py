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
large=0
slarge=0
for i in range (len(l)):
    if l[i]>large:
        slarge=large
        large=l[i]
    elif l[i]<large and l[i]>slarge:
        slarge=l[i]
print("The second largest element is: ",slarge)
