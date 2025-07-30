x = input("Enter the elements with spaces: ")
n = x.split()
k = int(input("Enter the k-th largest element: "))
lst = []
h=k
while(k):
    v = max(n)
    lst.append(v)
    n.remove(v)
    k=k-1

print(f"The {h}th largest element is: {lst[-1]}")
