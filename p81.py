str=input("Enter any string:")
vowels="AEIOU"
consta="BCDFGHJKLMNPQRSTVWXYZ"
al=d=s=ch=vo=con=0
for i in str:
    if i.upper() in vowels:
        vo+=1
    elif i.upper() is consta:
        con+=1
    if i.isalpha():
        al+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
print("Total number of characters are",len(str))
print("Total number of vowels are",vo)
print("Total number of consonants are",con)
print("Total number of spaces are",s)
print("Total number of digit are",d)
print("Total number of alphabet are",al)