while True:
    import math
    def squ(a):
        squ=a*a
        return squ
    def rect(l,b):
        rect=l*b
        return rect
    def cir(r):
        cir=math.pi*r*2
        return cir
    def tri(a,b,c):
        s=(a+b+c)/2
        tri=math.sqrt(s*(s-a)*(s-b)*(s-c))
        return tri
    def para(h,b):
        para=b*h
        return para
    def con(r,l):
        con=math.pi*r*(r+l)
        return con
    def cyl(r,h):
        cyl=2*math.pi*r*(r+h)
        return cyl
    def cub(a):
        cube=a**3
        return cube
    def cubo(l,b,h):
        cubo=l*b*h
        return cubo
    def sph(r):
        sph=(4/3)*math.pi*r**3
        return sph
    def h_sph(r):
        h_sph=(2/3)*math.pi*r**3
        return h_sph
    def cone(r,h):
        cone=math.pi*r**2*h
        return cone
    def cyli(r,h):
        cyli=math.pi*r**2*h
        return cyli
    def prog():
        print('''Menu of the program
    1.Area
    2.Volume''')
        ch=int(input("Enter your choice(1-2):"))
        if ch==1:
            while True:
                print('''Menu for area
        1.Area of Square
        2.Area of Rectrangle
        3.Area of Circle
        4.Area of Triangle
        5.Area of Paralellogram
        6.Area of Cone
        7.Area of Cylinder''')
                ch1=int(input("Enter your choice(1-7):"))
                if ch1==1:
                    a=int(input("Enter any number:"))
                    print("Area of Square is",squ(a))
                elif ch1==2:
                    l=int(input("Enter the length of rectrangle:"))
                    b=int(input("Enter the breadth of rectrangle:"))
                    print("Area of rectrangle is",rect(l,b))
                elif ch1==3:
                    r=int(input("Enter the radius of circle:"))
                    print("Area of circle is",cir(r))
                elif ch1==4:
                    a=int(input("Enter the first side:"))
                    b=int(input("Enter the second side:"))
                    c=int(input("Enter the third side:"))
                    print("Area of triangle is",tri(a,b,c))
                elif ch1==5:
                    h=int(input("Enter the height:"))
                    b=int(input("Enter the base:"))
                    print("Area of parallogram is",para(h,b))
                elif ch1==6:
                    r=int(input("Enter the radius:"))
                    h=int(input("Enter the height:"))
                    print("Area of cylinder is",cyl(h,r))
                elif ch1==7:
                    r=int(input("Enter the radius:"))
                    l=int(input("Enter the slant height:"))
                    print("Area of cone is",con(l,r))
                else:
                    print("Worng choice/Please try again")
                    continue
                Q=input("Do you want to find area again (Y/N):")
                if Q.upper()=="Y":
                    continue
                else:
                    break
        elif ch==2:
            while True:
                print('''Menu
    1.Volume of cube
    2.Volume of cuboid
    3.Volume of sphere
    4.Volume of hemisphere
    5.Volume of cone
    6.Volume of cylinder''')
                ch2=int(input("Enter your choice:"))
                if ch2==1:
                    a=int(input("Enter the side:"))
                    print("Volume of cube is",cub(a))
                elif ch2==2:
                    l=int(input("Enter the length:"))
                    b=int(input("Enter the breagth:"))
                    h=int(input("Enter the height:"))
                    print("Volume of cuboid is",cubo(l,b,h))
                elif ch2==3:
                    r=int(input("Enter the radius:"))
                    print("Volume of sphere is",sph(r))
                elif ch2==4:
                    r=int(input("Enter the radius:"))
                    print("Volume of hemisphere is",h_sph(r))
                elif ch2==6:
                    r=int(input("Enter the radius:"))
                    h=int(input("Enter the height:"))
                    print("Volume of cylinder is",cyli(r,h))
                elif ch2==5:
                    r=int(input("Enter the radius:"))
                    h=int(input("Enter the height:"))
                    print("Volume of cone is",con(r,h))
                else:
                    print("Worng choice/Please try again")
                    continue
                Q=input("Do you want to find volume again (Y/N):")
                if Q.upper()=="Y":
                    continue
                else:
                    break
        else:
            print("Worng choice/Please try again")
            continue
        Q=input("Do you want to continue (Y/N):")
        if Q.upper()=="Y":
            continue
        else:
            break
    prog()