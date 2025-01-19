#Write a program in python to take input in string and reverse it.
str=input("Enter any string: ")
s=str[::-1]
p=s.split()
q=p[::-1]
x=" ".join(q)
print("Tne reverse string is: ",x)
