#Write a program in python to print the following pattern:
#      *
#      *
#  * * * * *
#      *
#      *
n=int(input("Enter the number of lines: "))
for i in range (1,2*n):
        for j in range (1,2*n):
                if i==n or j==n:
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()
