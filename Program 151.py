#Write a program in python using function to print the following pattern:
#  1
#  1 2
#  1 2 3
#  1 2 3 4
def pattern(n):
    for i in range (1,n+1):
            for j in range (1,i+1):
                    print(j,end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
