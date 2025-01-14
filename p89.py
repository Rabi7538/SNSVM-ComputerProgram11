l=[]
while True:
    p=int(input("Enter the element:"))
    l.append(p)
    ch=input("Do you want to add more(Y/N):")
    if ch.upper()==y:
        continue
    else:
        break
print("the list is",l)
search=int(input("Enter the element you want to search:"))
flag=False
for i in range(len(l)):
    if l(i)==search:
        pos=i
        flag=True
        break
if flag==True:
    print("The search element %d if formed in %d position"%(search,pos+1))
else:
    print("The search element %d is not found "%(search))