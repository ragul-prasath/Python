'''
Write a Python program that takes a string and an integer max_width as input. 
The program should split the string into substrings of length max_width and print each substring on a new line.
eg: input: ABCDEFGHIJKLIMNOQRSTUVWXYZ
           4
    output: ABCD
            EFGH
            IJKL
            IMNO
            QRST
            UVWX
            YZ
'''
string=input("enter the string: ")
max_width=int(input("enter the slice: "))
string=list(string)
string1=[]
if(len(string)%max_width==0):
    n=0
    k=max_width
    for i in range(1,(len(string)//max_width)+1):
        string1=string[n:k]
        print("".join(string1))
        n=max_width+n
        k=k+max_width
else:
    n=0
    k=max_width
    for i in range(0,(len(string)//max_width)+1):
        if(i-1<(len(string)/max_width)):
            string1=string[n:k]
            print("".join(string1))
            n=max_width+n
            k=k+max_width
        else:
            string1=string[n:]
            print("".join(string1))
