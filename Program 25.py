#Write a program to print the following pattern:
#  * * * *
#   * * *
#    * *
#     *
n=int(input("Enter the number of rows: "))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
