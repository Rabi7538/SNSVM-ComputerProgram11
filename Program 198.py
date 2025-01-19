#Write a program in python using function to print the following pattern:
#      A
#     p A
#    p p A
#   l p p A
#  e l p p A
def pattern(str):
    for i in range (len(str)):
        p=i
        for j in range (len(str)-i):
            print(" ",end="")
        for k in range (i+1):
            print (str[p],end=" ")
            p-=1
        print()
def main():
    str=input("Enter any string: ")
    pattern(str)
main()
