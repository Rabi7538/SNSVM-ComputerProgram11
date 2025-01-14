l=[]
n=int(input("Now many element want to enter:"))
for i in range(n):
    p=int(input("Enter the %d element:"%(i+1)))
    l.append(p)
print("The list is",l)