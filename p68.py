#68
n=int(input("Enter any number: "))
p=n
sum=0
while p!=0:
  r=p%10
  fact=1
  for i in range(1,r+1):
    fact*=i
  sum+=fact
  p//=10
if sum==n:
  print("%d is a special number"%(sum))
else:
  print("%d is not a special number"%(sum))