#Write a program in python to print the following pattern:
#  * * * * * * 
#  * *     * * 
#  *         * 
#  * *     * * 
#  * * * * * * 
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
	for j in range (i,n+1):
		print("*",end=" ")
	for k in range (2,2*i):
		print(" ",end=" ")
	for l in range (i,n+1):
		print("*",end=" ")
	print()
for i in range (1,n):
	for j in range (0,i+1):
		print("*",end=" ")
	for k in range (2*(n-i-1),0,-1):
		print(" ",end=" ")
	for l in range (0,i+1):
		print("*",end=" ")
	print()