#Write a program in python to print the following pattern:
#  * * * * *
#    * * *
#      *
#    * * *
#  * * * * *
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
    for j in range (1,i+1):
        print(" ", end=" ")
    for k in range (2*(n-(i-1))-1,0,-1):
        print("*", end=" ")
    print()
for i in range (1,n):
	for j in range (2*(n-i),0,-1):
		print(" ",end="")
	for k in range (1,2*i+2):
		print("*",end=" ")
	print()
