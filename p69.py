#69
import math
n=int(input("Enter any number: "))
p=n
count=0
while p!=0:
  p//=10
  count+=1
p=n*n
q=p% math.pow(10,count)
if n==q:
  print("%d is a Automorphic number"%(n))
else:
  print("%d is not a  Automorphic number"%(n))