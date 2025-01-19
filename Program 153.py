#Write a program in python using function to print the following pattern:
#  4 3 2 1
#   3 2 1
#    2 1
#     1
def pattern(n):
    for i in range (n,0,-1):
            for j in range (n,i-1,-1):
                    print(" ",end="")
            for k in range (i,0,-1):
                    print(k,end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
