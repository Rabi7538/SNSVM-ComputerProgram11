#Write a program to print the following pattern:
#     *
#    * *
#   * * *
#  * * * *
n=int(input("Enter the number of rows: "))
for i in range (1,n+1):
    for j in range (n,i-1,-1):
        print(" ",end="")
    for j in range (1,j+1):
        print("*",end=" ")
    print()
