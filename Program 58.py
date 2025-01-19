#Write a program to find the sum of the following series:
#          1+2+3+4+5+......
n=int(input("Enter the number of terms: "))
sum=0
for i in range (1,n+1):
	sum+=i
print("Sum of the series is %d."%(sum))
