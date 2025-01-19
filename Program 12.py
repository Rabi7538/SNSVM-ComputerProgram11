#Write a program to find the area of square, rectangle, triangle, circle, cylinder, cone and parallelogram and also volume of cube, cuboid, sphere, cone and cylinder.
import math
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
                s=int(input("Enter the length of side: "))
                print("Area of square is",s*s)
            elif n==2:
                l=int(input("Enter the length: "))
                b=int(input("Enter the breadth: "))
                print("Area of rectangle is",l*b)
            elif n==3:
                a=int(input("Enter the first side: "))
                b=int(input("Enter the second side: "))
                c=int(input("Enter the third side: "))
                s=(a+b+c)/2
                area=math.sqrt(s*(s-a)*(s-b)*(s-c))
                print("Area of triangle is",area)
            elif n==4:
                r=int(input("Enter the radius: "))
                print("Area of circle is",math.pi*r*r)
            elif n==5:
                r=int(input("Enter the radius: "))
                h=int(input("Enter the height: "))
                print("Area of cylinder is",2*math.pi*r*(h+r))
            elif n==6:
                r=int(input("Enter the radius: "))
                h=int(input("Enter the height: "))
                l=math.sqrt((h*h)+(r*r))
                print("Area of cone is",math.pi*r*(l+r))
            elif n==7:
                b=int(input("Enter the base: "))
                h=int(input("Enter the height: "))
                print("Area of parallelogram is",b*h)
            else:
                print("Wrong Choice! Please try again.")
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
                s=int(input("Enter the length of side: "))
                print("Volume of cube is",s**3)
            elif o==2:
                l=int(input("Enter the length: "))
                b=int(input("Enter the breadth: "))
                h=int(input("Enter the height: "))
                print("Volume of cuboid is",l*b*h)
            elif o==3:
                r=int(input("Enter the radius: "))             
                print("Volume of sphere is",(4/3)*math.pi*r**3)
            elif o==4:
                r=int(input("Enter the radius: "))
                h=int(input("Enter the height: "))
                print("Volume of cone is",(1/3)*math.pi*r*r*h)
            elif o==5:
                r=int(input("Enter the radius: "))
                h=int(input("Enter the height: "))
                print("Volume of cylinder is",math.pi*r*r*h)
            else:
                print("Wrong Choice! Please try again.")
    else:
        print("Wrong Choice! Please try again.")
