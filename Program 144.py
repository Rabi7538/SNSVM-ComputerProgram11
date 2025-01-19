#Write a program in python using function to print the following pattern:
#  * * * * *
#  @ * * * @
#  @ @ * @ @
#  @ * * * @
#  * * * * *
def pattern(n):
    for i in range (1,n+1):
        for j in range (1,i):
            print ("@",end=" ")
        for k in range (2*(n-(i-1))-1,0,-1):
            print("*", end=" ")
        for l in range (2,i+1):
            print("@",end=" ")
        print()
    for i in range (1,n):
            for j in range (n-1,i,-1):
                    print("@",end=" ")
            for k in range (1,2*i+2):
                    print("*",end=" ")
            for l in range (n-1,i,-1):
                    print("@",end=" ")
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
