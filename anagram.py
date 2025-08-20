n=input("enter the 1st string with space: ")
n=n.replace(" ","")
lst1=list(n)
m=input("enter the 2nd string with space: ")
m=m.replace(" ","")
lst2=list(m)
lst1=sorted(lst1)
lst2=sorted(lst2)

if len(lst1)!=len(lst2):
    print("thos is not anagram")
else:
    if lst1==lst2:
        print("this is anagram")
    else:
        print("this is not anagram")

