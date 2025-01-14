#Write a program in python to print the following pattern. 
#           * 
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
def pat(n):
    for i in range(1,n+1):
        for j in range(2*i-1,2*n+1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()