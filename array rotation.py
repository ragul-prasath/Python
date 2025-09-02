lst=list(map(int,input("enter the numbers seperate by comma: ").split(",")))
k=int(input("enter the number of rotation: "))
lst1=lst.copy()
for i in range(k):
    for j in range(len(lst)):
        if(j!=len(lst)-1):
            lst1[j]=lst[j+1]
        else:
            lst1[j]=lst[0]
    lst = lst1.copy()
print(lst1)