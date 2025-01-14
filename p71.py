#71
n=int(input("Enter any number: "))
p=n
sum=0
while True:
  if p!=0:
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
    print("%d is a magic number"%(n))
else:
    print("%d is not a magic number"%(n))