#To find sum of consecutive prime number is prime number or not
n=int(input("Enter the range : "))
lst=[2]
for i in range(3,n+1):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
    if(count==0):
        lst.append(i)
sum=0
for i in range(len(lst)):
    sum=sum+lst[i]
r=0
for i in range(2,sum):
    if(sum%i==0):
        r=r+1
if(r==0):
    print(f"{sum} is prime number")
else:
    print(f"{sum} is not prime number")
    
