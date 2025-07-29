# move zero to right side of array.Eg: [6,0,4,0,9]=[6,4,9,0,0]
n=input("Enter the number :")
n=n.split(",")
for i in range(len(n)):
    n[i]=int(n[i])
for i in range(len(n)):
    if n[i]==0:
        n.pop(i)
        n.insert(-1,0)
print(n)