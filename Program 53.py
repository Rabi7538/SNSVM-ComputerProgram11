#Write a program in python to print the following pattern:
#        A
#      B A B
#    C B A B C
#  D C B A B C D
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
	ch=64+i
	for j in range (1,2*(n-i+1)):
		print(" ",end="")
	for k in range (1,2*i):
		if k<=i:
			print(chr(ch),end=" ")
			ch-=1
		else:
		    ch+=1
		    print(chr(ch+1),end=" ")
	print()
