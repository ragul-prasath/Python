n=input()
n=n.replace(" ","")
lst1=list(n)
m=input()
m=m.replace(" ","")
lst2=list(m)
lst1=sorted(lst1)
print(lst1)
lst2=sorted(lst2)
print(lst2)

if len(lst1)!=len(lst2):
    print("thos is not anagram")
else:
    if lst1==lst2:
        print("this is anagram")
    else:
        print("this is not anagram")

