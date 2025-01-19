#Write a program in python to print the following pattern:
#     1
#    2 3
#   4 5 6
#  7 8 9 10
n=int(input("Enter the number of lines: "))
c=1
for i in range (1,n+1):
	for j in range (n,i-1,-1):
		print(" ",end="")
	for k in range (1,i+1):
		print(c,end=" ")
		c+=1
	print()
