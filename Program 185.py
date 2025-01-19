#Write a program in python using function to count and print the palindrome number between certain range.
def palindrome(n):
    p=n
    sum=0
    while p!=0:
        s=p%10
        sum=sum*10+s
        p//=10
    return sum
def main():
    m=int(input("Enter the first range value: "))
    n=int(input("Enter the last range value: "))
    count=0
    for i in range (m,n+1):
        p=i
        if palindrome(p)==i:
            print(i,end=",")
            count+=1
    print("\nTotal palindrome number between %d and %d is %d."%(m,n,count))
main()
