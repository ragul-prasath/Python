rows = int(input("enter the number of rows: "))
a, b = 0, 1
for i in range(1, rows + 1):
    for j in range(i):
        print(a, end=" ")
        a, b = b, a + b  
    print()
