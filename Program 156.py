#Write a program in python using function to print the following pattern:
#  10 9 8 7
#    6 5 4
#     3 2
#      1
def pattern(n):
    for i in range (n,0,-1):
            c=i*(i+1)//2
            for j in range (1,n-i+2):
                    print(" ",end="")
            for k in range (1,i+1):
                    print(c,end=" ")
                    c-=1
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
