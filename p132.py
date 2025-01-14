#Write a program in python to print the following pattern.
# * * * * * * * * * 
#    * * * * * * * 
#      * * * * * 
#        * * * 
#          * 
#        * * * 
#      * * * * * 
#    * * * * * * * 
#  * * * * * * * * * 
def pat(n):
    for i in range(n,0,-1):
        for j in range(2*i-1,2*n):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end=" ")
        print()
    for  i in range (2,n+1):
        for j in range(2*i,n*2+1):
            print(" ",end="")
        for k in range(1,i*2):
            print("*",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()