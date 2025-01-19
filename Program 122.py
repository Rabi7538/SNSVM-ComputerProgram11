#Write a program in python using function to convert the ASCII character to its value and vice versa using menu driven technique.
def charactertovalue():
    n=input("Enter the ASCII character: ")
    print("ASCII character =",n,", ASCII value =",ord(n))
def valuetocharacter():
    n=int(input("Enter the ASCII value (0-127): "))
    print("ASCII value =",n,", ASCII character =",chr(n))
def main():
    print('''Menu of the Program:
1. ASCII character to ASCII value
2. ASCII value to ASCII character''')
    ch=int(input("Enter your choice: "))
    if ch==1:
        charactertovalue()
    elif ch==2:
        valuetocharacter()
    else:
        print("Wrong Choice")
main()
