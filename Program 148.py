#Write a program in python using function to print the following pattern:
#  *       *
#    *   *
#      *
#    *   *
#  *       *
def pattern(n):
    a=0
    b=n
    for i in range(n):
            for j in range(n):
                    if i==a or j==b:
                            print("*",end=" ")
                            a+=1
                            b-=1
                    elif i==j:
                            print("*",end=" ")
                    else:
                            print (" ",end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
