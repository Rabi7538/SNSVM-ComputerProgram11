#Write a program to print the following pattern:
#     *
#    * #
#   * # *
#  * # * #
n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range (1,n-i+2):
        print(" ",end="")
    for k in range (1, i+1):
        if k%2==0:
            print("#", end=" ")
        else:
        	print("*",end=" ")
    print()
