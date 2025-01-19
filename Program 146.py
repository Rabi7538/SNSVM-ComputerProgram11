#Write a program in python using function to print the following pattern:
#          *
#        *   *
#      *       *
#    *           *
#  * * * * * * * * *
def pattern(n):
    for i in range (1,n+1):
        for j in range (2*i-1,2*n):
            print(" ", end="")
        for k in range (1,2*i):
            if k==1 or k==2*i-1 or i==n:
                print("*", end=" ")
            else:
                    print(" ",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
