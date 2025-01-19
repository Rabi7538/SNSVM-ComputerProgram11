#Write a program to find the sum of the following series:
#        7x^7/7!-14x^14/14!+21x^21/21!....
n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
sum=0
for i in range (1,n+1):
    fact=1
    for j in range (1,7*i+1):
        fact*=j
    sum+=((-1)**(i+1))*(7*i)*(x**(7*i))/fact
print("Sum of the series is %f."%(sum))
