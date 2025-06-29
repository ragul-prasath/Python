n = int(input("Enter number of rows: "))
h = 1
for i in range(n):
    print("  " * (n - i - 1), end="")  
    for j in range(n):
        if(h<10):
            print(" " + str(h), end=" ")
            h=h+1
        else:
            print(str(h),end=" ")
            h += 1
    print()
