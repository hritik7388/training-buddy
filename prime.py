# print prime number 1to n
lower=int(input("enter the value:-"))
greater=int(input("enter the  value:-"))

for number in range(lower,greater+1):
    count=0
    for i in range(2,(number//2+1)):
        if(number%i==0):
            count=count+1
            break

        
    if(count==0 and number !=1):
         print("%d"%number,end='')
