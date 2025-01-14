def ascii_chr(val):
    char=chr(val)
    return chr
def ascii_chr(n):
    value=ord(n)
    return value
def main():
    print("""Menu of the program:
1.ASCII value to ASCII character
2.ASCII character of ASCII value""")
    ch=(int(input("Enter your choice:")))
    if ch==1:
        val=input("Enter the ASCII value(0-127):")
        v=ascii_chr(val)
        print("ASCII value",val,"ASCII character",v)
    