#Write a program in python using function to find the sum of the following series:
#        2-4+6-8+10-12+........
def series(n):
    sum=0
    for i in range (1,n+1):
            sum+=(-1)**(i+1)*(2*i)
    print("Sum of the series is %d."%(sum))
def main():
    n=int(input("Enter the number of terms: "))
    series(n)
main()
