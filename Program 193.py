#Write a program in python using function to take input in string and reverse it.
def reverse(str):
    for i in range (len(str)-1,-1,-1):
        print(str[i],end="")
def main():
    str=input("Enter any string: ")
    reverse(str)
main()
