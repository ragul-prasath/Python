n=5
alpha=65
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(alpha),end=" ")
        alpha=alpha+1
    alpha=65
    print()