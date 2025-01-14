#77
import math
m=int(input("Enter the first range value:"))
n=int(input("Enter the first range value:"))
count=0
for i in range(m,n+1):
  p=i
  c=0
  while p!=0:
    p//=10
    c+=1
  p=i*i
  q=p%math.pow(10,c)
  if q==i:
    count+=1
    print(i,end=",")
print("\nTotal automorphic numbers between %d and %d is %d"%(m,n,count))