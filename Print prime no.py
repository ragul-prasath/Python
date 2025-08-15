#Print prime number
n = int(input("Enter the limit: "))

for num in range(2, n + 1,1):            
    for i in range(2, num,1):             
        if num % i == 0:
            break                     
    else:
        print(num, end=" ")             
