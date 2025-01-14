import math
def que(a,b,c):
    if a==0:
        print("This is not a quadritic equation")
    else:
        d=b*b-4*a*c
        if d<0:
            print("This roots are imaginary")
        elif d==0:
            x=-b/2*a
            print("Root of the equation is",x)
        else:
            x1=(-b+math.sqrt(d))/2*a
            x2=(-b-math.sqrt(d))/2*a
            print("Roots of the equation is",x1,"and",x2)
def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=int(input("Enter the third number:"))
    print(que(a,b,c))
main()