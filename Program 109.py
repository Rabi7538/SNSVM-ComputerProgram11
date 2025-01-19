#Write a program in python to print the following pattern:
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
    for j in range (n,i-1,-1):
                    print(" ",end="")
    c=1
    for k in range (1,i+1):
                    print(c,end=" ")
                    c=c*(i-k)//k
    print()
