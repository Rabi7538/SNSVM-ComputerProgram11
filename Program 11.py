#Write a program in python using menu driven to convert the ASCII character to its value and vice versa.
while True:
    print('''Menu of the Program
1. ASCII character to ASCII value
2. ASCII value to ASCII character''')
    p='y'
    while p.upper()=='Y':
        ch=int(input("Enter your choice: "))
        if ch==1:
            s=input("Enter the ASCII character: ")
            print("ASCII character =",s,"ASCII value =",ord(s))
        elif ch==2:
            s=int(input("Enter the ASCII value(0-127): "))
            print("ASCII value =",s,"ASCII character =",chr(s))
        else:
            print("Wrong Choice! Please try again.")