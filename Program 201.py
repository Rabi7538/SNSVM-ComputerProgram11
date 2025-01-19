#Write a program in python using function to take input in a list and search the element using linear search technique.
def list():
    l=[]
    while True:
        p=int(input("Enter the element: "))
        l.append(p)
        ch=input("Do you want to add more(Y/N): ")
        if ch.upper()=='Y':
            continue
        else:
            break
    print("The list is",l)
    return la
def search(n,l):
    for i in range (len(l)):
        if l[i]==n:
            pos=i+1
            break
        return True,pos
    return False,pos
def main():
    l=list()
    n=int(input("Enter the element you want to search: "))
    flag,pos=search(n,l)
    if flag==True:
        print("The searched element %d is found in %d position."%(n,pos))
    else:
        print("The searched element %d is not found."%(n))
main()
