#1- print hello world
#a="hello ! world"
#print(a)

#2- add two integer

#x=int(input("enter the value of x:-"))
#y=int(input("enter the value of y:-"))
#sum=x+y
#print("total the sum of x and y is :-",sum)

#3- swap of two number with using 3rd variable
#a=int(input("enter the value of a:-"))
#b=int(input("enter the value of b:-"))
#temp=a
#a=b
#b=temp
#p#rint("# after swaping #")
#print("print the value of a",a)
#print("print the value of b",b)

 #
# 4-swaping without using 3rd var
#a=int(input("enter the value:-"))
#b=int(input("enter the value :-"))
#a=a+b
#b=a-b
#a=a-b
#print("##after swaping##")
#print("value of a:-",a)
#print("value of b:-",b)

# print prime number 1to n
#lower=int(input("enter the value:-"))
#greater=int(input("enter the  value:-"))

#for number in range(lower,greater+1):
  #  count=0
   # for i in range(2,(number//2+1)):
    #    if(number%i==0):
     #       count=count+1
      #      break

        
    #if(count==0 and number !=1):
     #   print("%d"%number,end='')


 # Armstrong number for n value
#x=int(input("Enter the value for armstrong number:--"))

#sum=0
#temp=x
#while temp>0:
  #    digit=temp%10
 #     sum+=digit**3
   #   temp//=10
#if x==sum:
 #     print("the value which is given by you is armstrong number")
      
#else:
#  print("the value which is given by you is not armstrong number")  
 
 
  
     
#2:- create a list and product of all the number  in a list

#list=["67","96","87","101","112","234","345"]
#n=int(input("enter the value hom wany time you want to product the number"))
#multiplied_list = [element * n for element in list]


#print(multiplied_list)
 
#write a program of largest number among three input number
#n1=int(input("enter the value for n1:-"))
#n2=int(input("enter the value for n2:-"))
#n3=int(input("enter the value for n3:-"))
#if (n1>n2) and (n1>n3):
 #     largest=num1
#elif (n2>n1) and (n2>n3):
 #     largest=n2
#else:
 #     largest=n3
  #    print("the largest number is :--",largest)

#write a program to check prime number or not
#x=int(input("enter the value "))
#if x>1:
  #    for i in range(2,int(x/2)+1):
   #         if(x%i)==0:
    #              print("is not a prime number")
     #             break
      #      else:
        #          print("is a prime number",x)
      
      #else:
            
        #    print("is not aprime number")

#length of list
#x=(34,56,87,98,35,45,5,5,5,6,7)
#print(len(x))

# addition of two list
list1=["aman","ajay","ankit","ajay",]
list2=["arun","ashish","nikhil","priyam"]
x=(list1+list2)
print(x)
             
    