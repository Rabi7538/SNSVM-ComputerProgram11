#Write a program in python using function to check whether a number is prime or not.
def prime(n):
    c=0
    for i in range (1,n//2+1):
        if n%i==0:
            c+=1
        if c==2:
            return False
    return True
def main():
    n=int(input("Enter the number: "))
    flag=prime(n)
    if flag==True:
        print(n,"is a prime number.")
    else:
        print(n,"is not a prime number.")
main()
