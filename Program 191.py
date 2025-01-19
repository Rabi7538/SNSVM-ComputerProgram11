#Write a program in python using function to count and print the magic number between certain range.
def magic(n):
    p=n
    while p>9:
        sum=0
        while p!=0:
            r=p%10
            sum+=r
            p//=10
        if sum>9:
            p=sum
    if sum==1:
        return True
    elif n==1:
        return True
    return False
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if magic(i)==True:
            print(i,end=",")
            count+=1
    print("\nTotal magic number between %d and %d is %d."%(m,n,count))
main()
