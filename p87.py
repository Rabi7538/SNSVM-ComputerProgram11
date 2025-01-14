str=input("Enter any string: ")
for i in range(len(str)):
    c=i
    for j in range(len(str),i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(str[c],end=" ")
        c-=1
    print()

