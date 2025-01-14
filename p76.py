#76
m=int(input("Enter the first range value: "))
n=int(input("Enter the second range value: "))
count=0
for i in range(m,n+1):
  p=i
  sum=0
  while p!=0:
    fact=1
    r=p%10
    for j in range(1,r+1):
      fact*=j
    sum+=fact
    p//=10
  if sum==i:
    count+=1
    print(i,end=",")
print("\nTotal special number between %d and %d is %d"%(m,n,count))