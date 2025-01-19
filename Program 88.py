#Write a program in python to print the following pattern:
#      A
#     p A
#    p p A
#   l p p A
#  e l p p A
str=input("Enter any string: ")
for i in range (len(str)):
    p=i
    for j in range (len(str)-i):
        print(" ",end="")
    for k in range (i+1):
        print (str[p],end=" ")
        p-=1
    print()
