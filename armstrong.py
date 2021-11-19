 # Armstrong number for n value
x=int(input("Enter the value for armstrong number:--"))

sum=0
temp=x
while temp>0:
      digit=temp%10
      sum+=digit**3
      temp//=10
if x==sum:
     print("the value which is given by you is armstrong number")
      
else:
  print("the value which is given by you is not armstrong number")  
 