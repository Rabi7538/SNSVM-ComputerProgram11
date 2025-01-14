#write a program in python to print  the follwing pattern.
#      A
#     A B
#    A B C
#   A B C D
#  A B C D E
def pat(n):
    for i in range(1,n+1):
        ch=65
        for j in range(n,i-1,-1):
            print(" ",end="")
        for k in range(1,i+1):
            print(chr(ch),end=" ")
            ch+=1
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()