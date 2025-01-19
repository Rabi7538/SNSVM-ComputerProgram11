#Write a program in python to print the following pattern:
#  * * * * * * *
#    * * * * *
#      * * *
#        *
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(" ", end=" ")
    for k in range (2*(n-(i-1))-1,0,-1):
        print("*", end=" ")
    print()
