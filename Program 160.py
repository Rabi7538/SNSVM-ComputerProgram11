#Write a program in python using function to print the following pattern:
#     A
#    A B
#   A B C
#  A B C D
def pattern(n):
    for i in range (1,n+1):
            ch=65
            for j in range (n,i-1,-1):
                    print(" ",end="")
            for k in range (1,i+1):
                    print(chr(ch),end=" ")
                    ch+=1
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
