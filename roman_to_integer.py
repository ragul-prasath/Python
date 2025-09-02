'''convert roman to integer
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
Eg: input= LVIII
    OUTPUT=58
    
    input: MCMXCIV
    output: 1994
'''
n=input("Enter the roman number: ")
n=list(n)
G=0
for i in range(len(n)):
        if(n[i]=='I'):
            n[i]=1
        elif(n[i]=='V'):
            n[i]=5
        elif(n[i]=='X'):
            n[i]=10
        elif(n[i]=='L'):
            n[i]=50
        elif(n[i]=='C'):
            n[i]=100
        elif(n[i]=='D'):
            n[i]=500
        elif(n[i]=='M'):
            n[i]=1000
        else:
            G=1
            break;
n=n[::-1]
count=n[0]
for i in range(len(n)-1):
    if(n[i]>n[i+1]):
        count=count-n[i+1]
    else:
        count=count+n[i+1]
print(count if(G!=1) else print('ENTER THE CORRECT ROMAN NUMBER''ENTER THE CORRECT ROMAN NUMBER'))
