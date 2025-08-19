'''
Find the no of sub string
string: ABCDCDC
sub_string: CDC
output: 2
'''
string=input("Enter the string: ")
string=list(string)
sub_string=input("Enter the sub string: ")
sub_string=list(sub_string)
low=0
count=0
high=len(sub_string)
for i in range(0,len(string)-len(sub_string)+1):
    if(sub_string==string[low:high]):
        count=count+1
    high=high+1
    low=low+1
print(count)