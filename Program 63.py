#Write a program to find the sum of the following series:
#       1-x/2!+x^2/3!-x^3/4!.......
n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
sum=0
for i in range (1,n+1):
    fact=1
    for j in range (1,i+1):
        fact*=j
    sum+=((-1)**(i+1))*(x**(i-1))/fact
print("Sum of the series is %f."%(sum))
