'''encrypt the message by adding 1 to all letter
input: abc123
output: bcd234
'''
n=input("enter the string: ")
l=[]
for i in range(len(n)):
    if(n[i].isdigit()):
        l.append(int(n[i])+1)
    else:
        k=ord(n[i])+1
        l.append(chr(k))
for i in range(len(l)):
    l[i]=str(l[i])
print("".join(l))