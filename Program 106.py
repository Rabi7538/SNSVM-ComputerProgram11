#Write a program in python to sort the rows of the matrix.
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
for i in range (m):
    for j in range (n):
        for k in range (n):
            if j+k<=n-1:
                if A[i][j]>A[i][j+k]:
                    A[i][j],A[i][j+k]=A[i][j+k],A[i][j]
for i in range (m):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
