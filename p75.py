#75
m=int(input("Enter the first range value: "))
n=int(input("Enter the second range value: "))
count=0
for i in range(m,n+1):
  sum=0
  for j in range(1,i//2+1):
    if i%j==0:
      sum+=j
  if sum==i:
    count+=1
    print(i,end=",")
print("\n Total perfect numbers between %d and %d is %d "%(m,n,count))
