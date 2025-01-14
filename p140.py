#write a program in python to print  the follwing pattern.
#      1 
#     2 3         
#    4 5 6        
#   7 8 9 10      
#  11 12 13 14 15 
def pat(n):
    f=1
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            print(" ",end="")
        for k in range(1,i+1):
            print(f,end=" ")
            f+=1
        print()
def main():
    n=int(input("Enter the number of lines:"))
    pat(n)
main()