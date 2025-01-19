#Write a program in python to take input in string and reverse it without changing the meaning of the word.
str=input("Enter any string: ")
s=str.split()
p=s[::-1]
q=" ".join(p)
print("Tne reverse string is: ",q)
