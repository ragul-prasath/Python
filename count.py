n=int(input("enter the element length: "))
lst=[]
for i in range(n):
    j=int(input("enter the element: "))
    lst.append(j)
count=1
for i in range(1,n):
    if(i==n or i==n-1):
        continue;
    elif(lst[i]<lst[i+1]):
        count=count+1
    else:
        continue;
print(count)
