#Write a progran in python to check whether a string is palindrome or not.
str=input("Enter any string: ")
flag=False
for i in range (len(str)//2):
    if str[i]==str[len(str)-i-1]:
        continue
    else:
        flag=True
        break
if flag==True:
    print(str,"is not a palindrome string.")
else:
    print(str,"is a palindrome string.")
