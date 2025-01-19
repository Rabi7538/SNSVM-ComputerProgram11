#Write a program in python using function to replace the vowels with '@' in a string.
def reverse(str):
    s=""
    for i in range (len(str)):
        if str[i].upper()=="A" or str[i].upper()=="E" or str[i].upper()=="I" or str[i].upper()=="O" or str[i].upper()=="U":
            s+='@'
        else:
            s+=str[i]
    print(s)
def main():
    str=input("Enter any string: ")
    reverse(str)
main()
