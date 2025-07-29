# you are given a 3 words. you should replace the vowels in first word with % and consonant in 2 word with #  and upper  the 3rd word
#eg: how are you - h%w#r#YOU
n=input("Enter the word: ")
n=n.split()
n1=n[0]
n2=n[1]
n3=n[2]
n1=list(n1)
n2=list(n2)
for i in range(len(n1)):
    if n1[i]=="a" or n1[i]=="e" or n1[i]=="i" or n1[i]=="o" or n1[i]=="u":
        n1[i]="%"
print("".join(n1),end=" ")
for j in range(len(n2)):
    if n2[j]=="a" or n2[j]=="e" or n2[j]=="i" or n2[j]=="o" or n2[j]=="u":
        continue;
    else:
        n2[j]="#"
print("".join(n2),end=" ")
print(n3.upper(),end=" ")
