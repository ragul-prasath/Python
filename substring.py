string=input("enter the number : ")
substring=[]
length=len(string)
m=[]
h=[]
count=0
for i in range(length):
    for j in range(i+1,length+1):
        substring.append(string[i:j])
for i in range(len(substring)):
    m.append(len(substring[i]))
for i in range(len(substring)):
    substring[i]=int(substring[i])
print(substring)
print(m)
sum=0
for i in range(len(substring)):
    l=substring(i)
    l=chr(l)
    l=list(l)
    for k in range(len(l)):
        l[k]=int(l[k])
    for j in range(len(l)):
        sum=sum+len[j]
    h.append(sum)
    sum=0
for i in range(len(h)):
    if h[i]==





