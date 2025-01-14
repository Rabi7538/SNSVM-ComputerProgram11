m=int(input("Enter the first range value:"))
n=int(input("Enter the second range value:"))
count=0
for i in range(m,n+1):
    p=i
    sum=0
    sum1=0
    while p!=0:
           r=p%10
           sum+=r
           p//=10
    q=sum
    while q!=0:
        s=q%10
        sum1=sum1*10+s
        q//=10
    if sum*sum==i:
            count+=1
            print(i,end=",")
print()
print("Total magic number between %d and %d is %d"%(m,n,count))