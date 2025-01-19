#Write a program in python to replace the vowels with '@' in a string.
str=input("Enter any string: ")
s=""
for i in range (len(str)):
    if str[i].upper()=="A" or str[i].upper()=="E" or str[i].upper()=="I" or str[i].upper()=="O" or str[i].upper()=="U":
        s+='@'
    else:
        s+=str[i]
print(s)
