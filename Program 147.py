#Write a program in python using function to print the following pattern:
#      *
#      *
#  * * * * *
#      *
#      *
def pattern(n):
    for i in range (1,2*n):
            for j in range (1,2*n):
                    if i==n or j==n:
                            print("*",end=" ")
                    else:
                            print(" ",end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
