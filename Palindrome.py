#Check whether string is palindrome or not
n=str(input("Enter the string : "))
n=list(n)
l=int(len(n)/2)
for i in range(l):
    if(n[i]!=n[-i-1]):
        print("NOT PALINDROME")
        break;
else:
    print("PALINDROME")