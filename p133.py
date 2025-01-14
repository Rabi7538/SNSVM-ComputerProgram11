#Write a program in python to print the following pattern.
# @ @ @ @ * @ @ @ @ 
# @ @ @ * * * @ @ @
# @ @ * * * * * @ @
# @ * * * * * * * @
# * * * * * * * * *
# @ * * * * * * * @
# @ @ * * * * * @ @
# @ @ @ * * * @ @ @
# @ @ @ @ * @ @ @ @
def pat(n):
    for i in range(1,n+1):
        for j in range(n,i,-1):
            print("@",end=" ")
        for k in range(1,2*i):
            print("*",end=" ")
        for m in range(n,i,-1):
            print("@",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(i,n):
            print("@",end=" ")
        for k in range(1,2*i):
            print("*",end=" ")
        for m in range(i,n):
            print("@",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()