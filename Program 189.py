#Write a program in python using function to count and print the neon number between certain range.
def neon(n):
    p=n*n
    sum=0
    while p!=0:
        r=p%10
        sum+=r
        p//=10
    return sum
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if neon(i)==i:
            print(i,end=",")
            count+=1
    print("\nTotal neon number between %d and %d is %d."%(m,n,count))
main()
