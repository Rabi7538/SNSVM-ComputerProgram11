#Write a program in python using function to print the following pattern:
#  J74 I73 H72 G71
#    F70 E69 D68
#      C67 B66
#        A65
#      B66 C67
#    D68 E69 F70
#  G71 H72 I73 J74
def pattern(n):
    for i in range (1,n+1):
            s=n-i+1
            ch=64+(s*(s+1)//2)
            for j in range (1,2*i):
                    print(" ",end="")
            for k in range (i,n+1):
                    print(chr(ch),ch,end=" ",sep="")
                    ch-=1
            print()
    ch=66
    for i in range (2,n+1):
            for j in range (1,2*(n-i+1)):
                    print(" ",end="")
            for k in range (1,i+1):
                    print(chr(ch),ch,end=" ",sep="")
                    ch+=1
            print()
def main():
    n=int(input("Enter the number of lines: "))
    pattern(n)
main()
