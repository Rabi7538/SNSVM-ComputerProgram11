#Write a program to find the sum of the following series:
#        -1/2!+2x^2/5!-3x^4/10!+4x^6/17!......
n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
sum=0
for i in range (1,n+1):
    fact=1
    for j in range (1,i**2+2):
        fact*=j
    sum+=((-1)**(i))*i*(x**(2*(i-1)))/fact
print("Sum of the series is %f."%(sum))
