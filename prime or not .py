#write a program to check prime number or not
x=int(input("enter the value "))
if x>1:
      for i in range(2,int(x/2)+1):
            if(x%i)==0:
                  print("is not a prime number")
                  break
            else:
                 print("is a prime number",x)
      
      else:
            
            print("is not aprime number")