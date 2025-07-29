# Find the rank of the list 
# Eg: [90,70,80,60,50] // output : [5,3,4,2,1]
n=input("Enter the number :")
n=n.split(",")
m=[]
for i in range(len(n)):
    n[i]=int(n[i])
l=sorted(n)
for i in range(len(n)):
    for j in range(len(l)):
        if n[i]==l[j]:
            m.append(j+1)
print(n)
print(m)