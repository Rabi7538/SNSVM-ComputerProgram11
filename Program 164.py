#Write a program in python using function to print the following pattern:
#  J I H G
#   F E D
#    C B
#     A
def pattern(n):
    for i in range (1,n+1):
            s=n-i+1
            ch=64+(s*(s+1)//2)
            for j in range (1,i+1):
                    print(" ",end="")
            for k in range (i,n+1):
                    print(chr(ch),end=" ")
                    ch-=1
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
