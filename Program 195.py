#Write a program in python using function to take input in string and reverse it.
def reverse(str):
    s=str[::-1]
    p=s.split()
    q=p[::-1]
    x=" ".join(q)
    print("Tne reverse string is: ",x)
def main():
    str=input("Enter any string: ")
    reverse(str)
main()
