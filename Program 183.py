#Write a program in python using function to check whether a number is magic or not.
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
    if sum==1 or n==1:
        return True
    else:
        return False
def main():
    n=int(input("Enter the number: "))
    if magic(n)==True:
        print("%d is a magic number."%(n))
    else:
        print("%d is not a magic number."%(n))
main()
