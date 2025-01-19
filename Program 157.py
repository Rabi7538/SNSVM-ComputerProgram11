#Write a program in python using function to print the following pattern:
#        1
#      1 2 1
#    1 2 3 2 1
#  1 2 3 4 3 2 1
def pattern(n):
    for i in range (1,n+1):
            c=1
            for j in range (2*n,2*i-1,-1):
                    print(" ",end="")
            for k in range (1,2*i):
                    if k<=i:
                            print(c,end=" ")
                            c+=1
                    else:
                            c-=1
                            print(c-1,end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
