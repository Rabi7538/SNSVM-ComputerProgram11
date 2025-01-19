#Write a program in python to take input in string and reverse it.
str=input("Enter any string: ")
for i in range (len(str)-1,-1,-1):
    print(str[i],end="")
