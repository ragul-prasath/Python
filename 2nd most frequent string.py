'''
to find second most frequent string
input : arr= [aaa,bbb,aaa,bbb,ccc,aaa]
output : bbb
explanation: aaa occur most time. the second most frequency is bbb
'''
arr=list(map(str,input("enter the string with comma: ").split(",")))
print(arr)
count=0
k=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i]==arr[j]):
            count=count+1
    if(count>k):
        k=count
        h=arr[i]
    count=0
l=[]
for i in range(len(arr)):
    if(arr[i]!=h):
        l.append(arr[i])
arr=[]
arr=l.copy()
count=0
k=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(arr[i]==arr[j]):
            count=count+1
    if(count>k):
        k=count
        h=arr[i]
    count=0
print(h)
