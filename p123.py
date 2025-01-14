#Write a program in python to print the following pattern
#      * 
#     * *
#    * * *
#   * * * *
#  * * * * *       
def pat(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for k in range(1,i+1):
            print("*",end=" ")
        print()
def main():
    n=int(input("Enter the number of liner:"))
    pat(n)
main()