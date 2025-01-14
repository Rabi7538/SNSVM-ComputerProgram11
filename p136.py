#write a program in python to print  the follwing pattern.
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****
def pat(n):
    for i in range(n,0,-1):
        for j in range(1,1+i):
            print("*",end="")
        for k in range(2*i-1,2*n):
            print(" ",end="")
        for m in range(1,i+1):
            print("*",end="")
        print()
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        for k in range(2*i-1,2*n):
            print(" ",end="")
        for m in range(1,i+1):
            print("*",end="")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()