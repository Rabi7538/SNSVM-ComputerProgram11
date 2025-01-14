#write a program in python to print  the follwing pattern.
#          1 
#        1 2 1
#      1 2 3 2 1
#    1 2 3 4 3 2 1
#  1 2 3 4 5 4 3 2 1
def pat(n):
    for i in range(1,n+1):
        c=1
        for j in range(2*n,2*i-1,-1):
            print(" ",end="")
        for k in range(1,2*i):
            if k<=i:
                print(c,end=" ")
                c+=1
            else:
                c-=1
                print(c-1,end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()