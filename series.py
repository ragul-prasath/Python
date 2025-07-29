# 1,1,2,3,4,9,8,27,16,81,32,243,64,729
# it combine two series(odd and even). find N th number
n=int(input("Enter the number: "))
c=1
s=1
for i in range(1,n+1):
    if i%2!=0:
        if n==i:
            print(f"the {i}th term of series is {c}")
        c=c+c 
    else:
        if n==i:
            print(f"the {i}th term of series is {s}")
        s=s*3
        