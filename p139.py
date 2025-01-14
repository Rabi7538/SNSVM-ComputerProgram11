#write a program in python to print  the follwing pattern.
#  5 4 3 2 1 
#   4 3 2 1  
#    3 2 1   
#     2 1    
#      1  
def pat(n):
    for i in range(n,0,-1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for k in range(i,0,-1):
            print(k,end=" ")
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()