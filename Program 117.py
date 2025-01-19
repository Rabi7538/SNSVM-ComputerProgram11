#Write a program in python using function to check whether a number is even or odd.
def evenodd(n):
    if n%2==0:
        return True
    else:
        return False
def main():
    n=int(input("Enter any number: "))
    flag=evenodd(n)
    if flag==True:
        print(n,"is an even number.")
    else:
        print(n,"is an odd number.")
main()
