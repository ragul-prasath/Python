# Find the rank of the list 
# Eg: [90,70,80,60,50] => Output: [5,3,4,2,1]

n = input("Enter the numbers separated by commas: ")
n = n.split(",")
m = []
for i in range(len(n)):
    n[i] = int(n[i])
l = sorted(n)
rank = {}
for i in range(len(l)):
    if l[i] not in rank:
        rank[l[i]] = i + 1
for i in range(len(n)):
    m.append(rank[n[i]])

print(n)
print(m)
