#Write a program in python using function to print the following pattern:
#     1
#    2 3
#   4 5 6
#  7 8 9 10
def pattern(n):
    c=1
    for i in range (1,n+1):
            for j in range (n,i-1,-1):
                    print(" ",end="")
            for k in range (1,i+1):
                    print(c,end=" ")
                    c+=1
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
