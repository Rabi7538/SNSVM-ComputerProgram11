#Write a program in python using function to count and print the special number between certain range.
def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
def special(n):
    p=n
    sum=0
    while p!=0:
        r=p%10
        sum+=factorial(r)
        p//=10
    return sum
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if special(i)==i:
            print(i,end=",")
            count+=1
    print("\nTotal special number between %d and %d is %d."%(m,n,count))
main()
