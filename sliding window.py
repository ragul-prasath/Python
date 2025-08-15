'''
you are given a array of integer and integer.your task is to find and print the maximum number in each contiguous window of size k.
input:
arr=[1,3,-1,-3,5,3,6,7]
k=3
output:
[3,3,5,5,6,7]
'''
arr = list(map(int, input("Enter numbers separated by comma: ").split(",")))
k=int(input("enter the integer: "))
l=[]
s=[]
for i in range(len(arr)-(k-1)):
    l=arr[i:k+i]
    l=sorted(l)
    s.append(l[-1])
    l=[]
print(s)
