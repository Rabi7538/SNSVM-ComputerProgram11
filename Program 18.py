#Write a program to print the following pattern:
#  *
#  * *
#  * * *
#  * * * *
n=int(input("Enter the number of rows: "))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    i+=1
    print()
