#write a program in python to print  the follwing pattern.
# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
def pat(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
def main():
    n=int(input("Enter the nuber of lines:"))
    pat(n)
main()