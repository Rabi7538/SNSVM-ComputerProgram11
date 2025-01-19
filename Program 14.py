#Write a program in python to find the prime number between certain range.
m=int(input("Enter the first range value: "))
n=int(input("Enter the last range value: "))
count=0
for num in range (m,n+1):
    c=0
    for i in range (1,num//2+1):
        if num%i==0:
            c+=1
    if c==1:
        print(num, end=",")
        count+=1
print("Total prime numbers between %d and %d is %d."%(m,n,count))
