#Write a program in python using function to print the following pattern:
#        *
#      * *
#    * * *
#  * * * *
def pattern(n):
    for i in range (1,n+1):
        for j in range (1,n-i+1):
            print(" ",end=" ")
        for j in range (1,i+1):
            print("*",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
