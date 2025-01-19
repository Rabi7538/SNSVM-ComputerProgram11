#Write a progran in python using function to check whether a string is palindrome or not.
def palin(str):
    flag=True
    for i in range (len(str)//2):
        if str[i]==str[len(str)-i-1]:
            continue
        else:
            return False
    return True
def main():
    str=input("Enter any string: ")
    flag=palin(str)
    if flag==True:
        print(str,"is a palindrome string.")
    else:
        print(str,"is not a palindrome string.")
main()
