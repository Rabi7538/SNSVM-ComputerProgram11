#Write a program in python to print the following pattern:
#     A
#    B A
#   C B A
#  D C B A
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
	ch=65+i-1
	for j in range (n,i-1,-1):
		print(" ",end="")
	for k in range (1,i+1):
		print(chr(ch),end=" ")
		ch-=1
	print()
