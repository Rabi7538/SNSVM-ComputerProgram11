#Write a program in python using function to print the second largest number among n numbers given by user.
def slarge():
    n=int(input("How many numbers want to enter: "))
    large=0
    slarge=0
    for i in range (n):
        p=int(input("Enter the %d number: "%(i+1)))
        if p>large:
            slarge=large
            large=p
        elif p<large and p>slarge:
            slarge=p
    return slarge
def main():
    print("Second largest number is %d."%(slarge()))
main()
