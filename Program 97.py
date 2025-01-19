l=[]
while True:
    p=int(input("Enter the value: "))
    l.append(p)
    ch=input("Do you want to add more(Y/N): ")
    if ch.upper()=='Y':
        continue
    else:
        break
print("The list is",l)
j=0
for i in range (len(l)):
    if l[j]<0:
        q=l.pop(j)
        l.append(q)
        j-=1
    j+=1
print("The updated list is:",l)
