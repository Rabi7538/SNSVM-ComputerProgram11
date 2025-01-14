m=int(input("Enter the first range value:"))
n=int(input("Enter the second range value:"))
count=0
for i in range(m,n+1):
    p=i
    sum=0
    while True:
        while p!=0:
           r=p%10
           sum+=r
           p//=10
        if sum>9:
            p=sum
            sum=0
        else:
            q=sum
            break
        if q==1:
            count+=1
            print(i,end=",")
print()
print("Total magic number between %d and %d is %d"%(m,n,count))
