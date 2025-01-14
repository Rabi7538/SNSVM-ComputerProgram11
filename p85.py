str=input("Enter any string:")
vowels="AEIOUaeiou"
word=" "
for i in str:
    if i in vowels:
        word+='@'
    else:
        word+=i
print(word)