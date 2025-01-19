#Write a program in python using function to count and print the armstrong number between certain range.
def armstrong(n):
    p=n
    sum=0
    c=0
    while p!=0:
       c+=1
       p//=10
    p=n
    while p!=0:
        r=p%10
        sum+=r**c
        p//=10
    return sum
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if armstrong(i)==i:
            print(i,end=",")
            count+=1
    print("\nTotal armstrong number between %d and %d is %d."%(m,n,count))
main()
