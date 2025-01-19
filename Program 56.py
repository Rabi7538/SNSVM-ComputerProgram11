#Write a program in python to print the following pattern:
#  J74 I73 H72 G71
#    F70 E69 D68
#      C67 B66
#        A65
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
	s=n-i+1
	ch=64+(s*(s+1)//2)
	for j in range (1,2*i):
		print(" ",end="")
	for k in range (i,n+1):
		print(chr(ch),ch,end=" ",sep="")
		ch-=1
	print()
