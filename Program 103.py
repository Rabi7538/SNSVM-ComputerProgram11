#Write a program in python to find the sum of the diagonals of the square matrix.
n=int(input("Enter the number of rows/columns of the square matrix: "))
sum=0
A=[[0 for col in range (n)]for row in range (n)]
print("Enter the value is the matrix:")
print("_"*50)
for i in range (n):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("The matrix is:")
print("_"*20)
for i in range (n):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
for i in range (n):
    for j in range (n):
        if i==j or (i+j)==(n-1):
            sum+=A[i][j]
print("Sum of the diagonals is %d."%(sum))
