n=input()
n=n.split(",")
for i in range(len(n)):
    n[i]=int(n[i])
k=len(n)
rs=sum(n)
rs=rs-n[0]
rs=rs-n[1]
ls=n[0]
for i in range(1,k-2):
    if ls==rs:
        print(n[i])
        break;
    else:
        ls=ls+n[i]
        rs=rs-n[i+1]
