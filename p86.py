str=input("Enter any string:")
for i in range(len(str)):
    for j in range(len(str),i-1):
        print(" ",end="  ")
    for k in range(i+1):
        print(str[k],end=" ")
    print()