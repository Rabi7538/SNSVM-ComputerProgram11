#Write a program in python using function to find the sum of the following series:
#        1/4-4/9+9/16-16/25+........
def series(n):
    sum=0
    for i in range (1,n+1):
            sum+=(-1)**(i+1)*((i**2)/(i+1)**2)
    print("Sum of the series is %f."%(sum))
def main():
    n=int(input("Enter the number of terms: "))
    series(n)
main()
