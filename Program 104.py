#Write a program in python to print the upper half and the lower half of the primary diagonal.
n=int(input("Enter the number of rows/columns of the square matrix: "))
A=[[0 for col in range (n)]for row in range (n)]
print("Enter the value is the matrix:")
print("_"*40)
for i in range (n):
    for j in range (n):
        A[i][j]=int(input("Enter the value in [%d][%d] position: "%(i,j)))
print("The matrix is:")
print("_"*20)
for i in range (n):
    for j in range (n):
        print("{0:^3}".format(A[i][j]),end="")
    print()
print("The upper half of the mtrix is:")
print("_"*40)
for i in range (n):
    for j in range (n):
        if i<=j:
            print(A[i][j],end="  ")
        else:
            print(" ",end="  ")
    print()
print("The lower half is: ")
print("_"*40)
for i in range (n):
    for j in range (n):
        if i>=j:
            print(A[i][j],end="  ")
    print()
