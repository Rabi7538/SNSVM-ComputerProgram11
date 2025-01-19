#Write a program in pythom using function to find the roots of thr quadratic equation.
import math
def quadratic(a,b,c):
    if a==0:
        print("This is not a quadratic equation.")
    else:
        d=b*b-4*a*c
        if d<0:
            print("Roots are imaginary.")
        elif d==0:
            x=-b/(2*a)
            print("Root of the quadratic equation is %f."%(x))
        else:
            x1=-b+math.sqrt(d)/(2*a)
            x2=-b-math.sqrt(d)/(2*a)
            print("Roots of the equation are %f and %f."%(x1,x2))
def main():
    a=int(input("Enter the coefficient of x^2: "))
    b=int(input("Enter the coefficient of x: "))
    c=int(input("Enter the constant value: "))
    quadratic(a,b,c)
main()
