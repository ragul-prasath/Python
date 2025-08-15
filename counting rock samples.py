'''EXAMPLE 1
INPUT : 10 2 (10 sample , 2 range)
345 604 320 433 704 470 808 718 811 (10 sample)
300 350 (range 1)
400 700 (range 2)
Output : 2, 4

There are 10 sample and 2 range. the sample are 345 604 320 433 704 470 808 718 811
the number of sample in each range are 2, 4 '''
n=input("enter the sample and no of range: ")
n=n.split()
for i in range(len(n)):
    n[i]=int(n[i])
l=input("Enter the samples: ")
l=l.split()
for i in range(len(l)):
    l[i]=int(l[i])  
k=1
lst=[]
while(k<=n[1]):
    h=input(f"enter the range {k} : ")
    h=h.split()
    for i in range(len(h)):
        h[i]=int(h[i])
    lst.append(h)
    h=[]
    k=k+1
s=[]
for i in range(len(lst)):
    count=0
    for k in range(len(l)):
        if(l[k]>lst[i][0] and l[k]<lst[i][1]):
            count=count+1
    s.append(count)
print(' '.join(map(str,s)))

