'''
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
eg: Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 
'''
s=input("enter the string: ")
l=list(s)
for i in range(len(l)):
    if(l[i].isupper()):
        l[i]=l[i].lower()
    elif(l[i].islower()):
        l[i]=l[i].upper()
    else:
        continue;
print(''.join(l))