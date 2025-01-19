#Write a program in python to print the following pattern:
#  1 2 3 4
#  1 2 3
#  1 2
#  1
n=int(input("Enter the number of lines: "))
for i in range (n,0,-1):
	for j in range (1,i+1):
		print(j,end=" ")
	print()
