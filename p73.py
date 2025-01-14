from os import sep
#73
m=int(input("Enter the first range value: "))
n=int(input("Enter the second range value: "))
count=0
for i in range(m,n+1):
  p=i
  sum=0
  while p!=0:
    r=p%10
    sum=sum*10+r
    p//=10
  if sum==1:
    count+=1
    print(i,end=",",sep=" ")
print("\nTotal palindrone number between %d and %d is %d"%(m,n,count))