#Write a program in python to check whether a number is prime or not.
num=int(input("Enter any number: "))
c=0
for i in range (1,num//2+1):
    if num%i==0:
        c+=1
if c==1:
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")