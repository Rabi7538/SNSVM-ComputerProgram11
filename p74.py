#74
m=int(input("Enter the first range value: "))
n=int(input("Enter the second range value: "))
for i in range(m,n+1):
  p=i
  c=0
  while p!=0:
    c+=1
    p//=10
  p=i
  count=0
  while p!=0:
    r=p%10
    s+=r**c
  if s==i:
    count+=1
    print(i,end=",")
print("\nIn total number of Armstrong number between %d and %d is %d "%(m,n,count))


