#Write a program in python to find the multiplication of two matrices.
m=int(input("Enter the number of rows of the first matrix: "))
n=int(input("Enter the number of columns of the first matrix: "))
p=int(input("Enter the number of rows of the second matrix: "))
q=int(input("Enter the number of columns of the second matrix: "))
A=[[0 for col in range (n)]for row in range (m)]
B=[[0 for col in range (q)]for row in range (p)]
C=[[0 for col in range (q)]for row in range (m)]
if n==p:
    print("Enter the value in first matrix:")
    print("_"*50)
    for i in range (m):
        for j in range (n):
            A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
    print("Enter the value in second matrix:")
    print("_"*50)
    for i in range (p):
        for j in range (q):
            B[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
    for i in range (m):
        for j in range (q):
            C[i][j]=0
            for k in range (n):
                C[i][j]+=A[i][k]*B[k][j]
    print("First matrix is:")
    print("_"*20)
    for i in range (m):
        for j in range (n):
            print("{0:^3}".format(A[i][j]),end="")
        print()
    print("Second matrix is:")
    print("_"*20)
    for i in range (p):
        for j in range (q):
            print("{0:^3}".format(B[i][j]),end="")
        print()
    print("Multiplication of two matrices is:")
    print("_"*30)
    for i in range (m):
        for j in range (q):
            print("{0:^3}".format(C[i][j]),end="")
        print()
else:
    print("Matrix multiplication is not possible.")
