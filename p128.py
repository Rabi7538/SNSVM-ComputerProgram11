#Write a program in python to print the following pattern
#      * 
#     * *
#    * # *
#   * # # *
#  * * * * *
def pat(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(" ",end="")
        for k in range(1,i+1):
            if k==1 or k==i or i==n:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()