#Write a program in python using function to take input in string and reverse it without changing the meaning of the word.
def reverse(str):
    s=str.split()
    p=s[::-1]
    q=" ".join(p)
    print("Tne reverse string is: ",q)
def main():
    str=input("Enter any string: ")
    reverse(str)
main()
