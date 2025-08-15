'''
given an array of integer, find the nearest smallest number for every element such that the smaller element is on left side
if smaller element not found print -1
eg: input=[1,6,4,10,2,5]
output= [-1,1,1,4,1,2]
'''
n=list(map(int,input("enter the element with comma: ").split(",")))
l=[]
for i in range(len(n)):
    for j in range(i-1,-1,-1):
        if(n[i]>n[j]):
            l.append(n[j])
            break;
    else:
        l.append(-1)
print(l)
