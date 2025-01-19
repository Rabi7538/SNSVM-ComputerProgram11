#Write a program to find the sum of the following series:
#        1+1/2+1/3+1/4+.......
n=int(input("Enter the number of terms: "))
sum=0
for i in range (1,n+1):
	sum+=1/i
print("Sum of the series is %f."%(sum))
