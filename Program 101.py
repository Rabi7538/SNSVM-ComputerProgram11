#Write a program in python to tranpose a matrix.
m=int(input("Enter the number of rows of matrix: "))
n=int(input("Enter the number of columns of matrix: "))
A=[[0 for col in range (n)]for row in range (m)]
print("Enter the value in the matrix:")
print("_"*30)
for i in range (m):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("The matrix is")
print("_"*20)
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
print("Tranpose of the matrix is:")
print("_"*20)
for i in range (n):
    for j in range (m):
        print("{0:^3}".format(A[j][i]),end="")
    print()
