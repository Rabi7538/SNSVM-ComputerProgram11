#Write a program in python using function to print the following pattern:
#  *
#  * *
#  * * *
#  * * * *
def pattern(n):
    i=1
    while i<=n:
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
        i+=1
        print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
