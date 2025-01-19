#Write a program in python to sort the matrix.
m=int(input("Enter the number of rows of the matrix: "))
n=int(input("Enter the number of columns of the matrix: "))
A=[[0 for col in range (n)]for row in range (m)]
print("Enter the value in the matrix: ")
print("_"*40)
for i in range (m):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("The matrix is:")
print("_"*20)
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
print("The updated matrix is:")
print("_"*30)
list=[item for sublist in A for item in sublist]
list.sort()
s=0
for i in range (m):
    for j in range (n):
        print("",list[s],end=" ")
        s+=1
    print()
