n=int(input("Enter the number of lines:"))
for i in range(n,0,-1):
    ch=65+i*(i+1)//2-1
    for j in range(1,n-i+2):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(ch),ch,end=" ",sep=" ")
        ch-=1
    print()
for i in range(2,n+1):
    ch=65+i*(i+1)//2+(i-1)
    for j in range(1,n-i+2):
        print(" ",end="")
    for k in range(1,i+1):
        print(chr(ch),ch,end=" ",sep=" ")
        ch-=1
    print()