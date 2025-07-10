n=int(input("enter the range: "))
a=1
b=1
for i in range(n):
    a,b=b,a+b
print(b-1)