# wap that take input 10numbers from user and
  #add  all even numbers.
  #add all odd numbers.
  #count odd and even.
  
k=0
j=0
temp=0
odd=0

l=int(input("enter how many number you want to count:"))
for i in range(0,1):
    a=int(input("enter number:"))
    if a%2==0:
        print(a,"is even number:")
        k=k+1
        temp=temp+a
    else:
        j=j+1
        odd=odd+a
        print(a,"is odd number:")
    print("total number of even number:")
    print("total number of add number:")
    print("addition of even number:")
    print("addition of odd number:")
