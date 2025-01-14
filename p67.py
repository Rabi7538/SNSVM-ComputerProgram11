#67
n=int(input("Enter any number: "))
p=n
sum=0
while p!=0:
  r=p%10
  sum+=r**3
  p//=10
if sum==n:
  print("%d is Armstrong number"%(n))
else:
  print("%d is not a Armstrong number"%(n))