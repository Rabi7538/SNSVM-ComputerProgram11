#Write a program in python using function to find the sum of the following series:
#        1+x+x^2+x^3+......
def series(n,x):
    sum=0
    for i in range (1,n+1):
        sum+=x**(i-1)
    print("Sum of the series is %d."%(sum))
def main():
    n=int(input("Enter the number of terms: "))
    x=int(input("Enter the value of x : "))
    series(n,x)
main()
