#Write a program in python using function to find the area of square, rectangle, triangle, circle, cylinder, cone and parallelogram and also volume of cube, cuboid, sphere, cone and cylinder.
import math
def areasq():
    s=int(input("Enter the length of side: "))
    print("Area of square is",s*s)
def arearec():
    l=int(input("Enter the length: "))
    b=int(input("Enter the breadth: "))
    print("Area of rectangle is",l*b)
def areatri():
    a=int(input("Enter the first side: "))
    b=int(input("Enter the second side: "))
    c=int(input("Enter the third side: "))
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of triangle is",area)
def areacir():
    r=int(input("Enter the radius: "))
    print("Area of circle is",math.pi*r*r)
def areacyl():
    r=int(input("Enter the radius: "))
    h=int(input("Enter the height: "))
    print("Area of cylinder is",2*math.pi*r*(h+r))
def areacone():
    r=int(input("Enter the radius: "))
    h=int(input("Enter the height: "))
    l=math.sqrt((h*h)+(r*r))
    print("Area of cone is",math.pi*r*(l+r))
def areapar():
    b=int(input("Enter the base: "))
    h=int(input("Enter the height: "))
    print("Area of parallelogram is",b*h)
def volcube():
    s=int(input("Enter the length of side: "))
    print("Volume of cube is",s**3)
def volcuboid():
    l=int(input("Enter the length: "))
    b=int(input("Enter the breadth: "))
    h=int(input("Enter the height: "))
    print("Volume of cuboid is",l*b*h)
def volsphere():
    r=int(input("Enter the radius: "))             
    print("Volume of sphere is",(4/3)*math.pi*r**3)
def volcone():
    r=int(input("Enter the radius: "))
    h=int(input("Enter the height: "))
    print("Volume of cone is",(1/3)*math.pi*r*r*h)
def volcyl():
    r=int(input("Enter the radius: "))
    h=int(input("Enter the height: "))
    print("Volume of cylinder is",math.pi*r*r*h)
def main():
    while True:
        print('''Menu of the program
1.Area
2.Volume''')
        m=int(input("Enter your choice: "))
        if m==1:
            while True:
                print('''Menu of program
1.Area of Square
2.Area of Rectangle
3.Area of Triangle
4.Area of Circle
5.Area of Cylinder
6.Area of Cone
7.Area of Parallelogram''')
                n=int(input("Enter your choice: "))
                if n==1:
                    areasq()
                elif n==2:
                    arearec()
                elif n==3:
                    areatri()
                elif n==4:
                    areacir()
                elif n==5:
                    areacyl()
                elif n==6:
                    areacone()
                elif n==7:
                    areapar()
                else:
                    ch=input("Wrong Choice! Do you wanna try again (Y/N): ")
                    if ch.upper()=='Y':
                        continue
                    else:
                        break
        elif m==2:
            while True:
                print('''Menu of the program
1.Volume of Cube
2.Volume of Cuboid
3.Volume of Sphere
4.Volume of Cone
5.Volume of Cylinder''')
                o=int(input("Enter your choice: "))
                if o==1:
                    volcube()
                elif o==2:
                    volcuboid()
                elif o==3:
                    volsphere()
                elif o==4:
                    volcone()
                elif o==5:
                    volcyl()
                else:
                    ch=input("Wrong Choice! Do you wanna try again (Y/N): ")
                    if ch.upper()=='Y':
                        continue
                    else:
                        break
        else:
            ch=input("Wrong Choice! Do you wanna try again (Y/N): ")
            if ch.upper()=='Y':
                continue
            else:
                break
main()
