#Write a program in python to print the following pattern   
#      * 
#     # #
#    * * *
#   # # # #
#  * * * * *
def pat(n):
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for k in range(1,i+1):
            if i%2!=0:
                print("*",end=" ")
            else:
                print("#",end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()