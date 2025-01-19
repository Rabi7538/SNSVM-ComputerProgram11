#Write a program in python to print the primary and secondary diagonal of the square matrix.
n=int(input("Enter the number of rows/columns of the square matrix: "))
A=[[0 for col in range (n)]for row in range (n)]
print("Enter the value is the matrix")
print("_"*50)
for i in range (n):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("The matrix is")
print("_"*20)
for i in range (n):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
print("The primary diagonal is")
print("_"*50)
for i in range (n):
    for j in range (n):
        if i==j:
            print(A[i][j],end=" ")
print()
print("The secondary diagonal is")
print("_"*50)
for i in range (n):
    for j in range (n):
        if (i+j)==(n-1):
            print(A[i][j],end=" ")
