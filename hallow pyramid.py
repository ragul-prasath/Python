#hallow pyramid
n =int(input("Enter the no of rows: "))
h = 1    

for i in range(1, n+1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "*" + " " * h + "*")
        h = h + 2  
