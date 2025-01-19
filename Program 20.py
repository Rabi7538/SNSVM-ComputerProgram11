#Write a program to print the following pattern (while loop):
#        *
#      * *
#    * * *
#  * * * *
n=int(input("Enter the number of rows: "))
i=1
while i<=n:
	j=n
	k=1
	while j>=i:
		print(" ",end=" ")
		j-=1
	while k<=i:
		print("*",end=" ")
		k+=1
	i+=1
	print()
