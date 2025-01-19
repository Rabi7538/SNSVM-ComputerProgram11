#Write a program in python to take input as string and count the total number of alphabets, digits, spaces, characters, vowels, consonants.
str=input("Enter any string: ")
vowels="AEIOU"
consonants="BCDFGHJKLMNPQRSTVWXYZ"
al=d=s=vo=con=0
for i in str:
    if i.upper() in vowels:
        vo+=1
    elif i.upper() in consonants:
        con+=1
    if i.isalpha():
        al+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
print("Total number of characters are %d."%(len(str)))
print("Total number of alphabets are %d."%(al))
print("Total number of digits are %d."%(d))
print("Total number of spaces are %d."%(s))
print("Total number of vowels are %d."%(vo))
print("Total number of consonants are %d."%(con))
