#Write a pogram to print the following pattern:
#  *       *
#    *   *
#      *
#    *   *
#  *       *
n=int(input("Enter the number of lines: "))
a=0
b=n
for i in range(n):
        for j in range(n):
                if i==a or j==b:
                        print("*",end=" ")
                        a+=1
                        b-=1
                elif i==j:
                        print("*",end=" ")
                else:
                        print (" ",end=" ")
        print()
