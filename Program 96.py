l=[]
while True:
    p=int(input("Enter the value: "))
    l.append(p)
    ch=input("Do you want to add more(Y/N): ")
    if ch.upper()=='Y':
        continue
    else:
        break
l.sort()
print("The list is",l)
flag=False
search=int(input("Enter the value you want to search: "))
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]<search:
        low=mid+1
    elif l[mid]>search:
        high=mid-1
    else:
        flag=True
        pos=mid+1
        break
if flag==True:
    print("The searched value %d is found in %d position."%(search,pos))
else:
    print("The searched value %d is not found."%(search))
