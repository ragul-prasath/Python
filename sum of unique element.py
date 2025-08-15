'''
sum of unique element in array
eg: input =[1,3,2,3,2,4]
output= 10
'''
arr=list(map(int,input("enter the element seperated by comma : ").split(",")))
s=[0]
count=0
for i in range(len(arr)):
    for j in range(len(s)):
        if(arr[i]==s[j]):
            count=count+1
    if(count==0):
        s.append(arr[i])
    count=0
s.pop(0)
count=0
for i in range(len(s)):
    count=count+s[i]
print(count)
