str=input("Enter any string: ")
for i in range(len(str)-1,-1,-1):
    print(str[i],end=" ")
word=" "
for i in range(len(str)-1,-1,-1):
    word+=str[i]
print("\nThe reverse string is",word)