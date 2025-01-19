#Write a program in python to print the following pattern:
#      A
#     A p
#    A p p
#   A p p l
#  A p p l e
str=input("Enter any String: ")
for i in range (len(str)):
    for j in range (len(str),i,-1):
        print(" ",end="")
    for k in range (i+1):
        print (str[k],end=" ")
    print()
