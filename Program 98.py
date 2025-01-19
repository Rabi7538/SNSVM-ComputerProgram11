#Write a program in python to find the sum of two matrices.
m=int(input("Enter the number of rows of the matrix: "))
n=int(input("Enter the number of columns of the matrix: "))
A=[[0 for col in range (n)]for row in range (m)]
B=[[0 for col in range (n)]for row in range (m)]
C=[[0 for col in range (n)]for row in range (m)]
print("Enter the value in 1st matrix:")
print("_"*50)
for i in range (m):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("Enter the value in 2nd matrix:")
print("_"*50)
for i in range (m):
    for j in range (n):
        B[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
for i in range (m):
    for j in range (n):
        C[i][j]=A[i][j]+B[i][j]
print("First matrix is:")
print("_"*20)
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
print("Second matrix is:")
print("_"*20)
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(B[i][j]),end="")
    print()
print("Sum of two matrices is:")
print("_"*30)
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(C[i][j]),end="")
    print()
