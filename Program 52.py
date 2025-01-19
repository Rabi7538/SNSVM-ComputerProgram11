#Write a program in python to print the following pattern:
#        A
#      A B A
#    A B C B A
#  A B C D C B A
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    ch=65
    for j in range (2*n,2*i-1,-1):
        print(" ", end="")
    for k in range(1,2*i):
        if k <=i:
            print(chr(ch), end=" ")
            ch+=1
        else :
            ch-=1
            print(chr(ch-1), end=" ")
    print()
