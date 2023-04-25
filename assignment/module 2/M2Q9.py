#write a python program to sum of three given integers.however, if two values are equal sum will be zero


a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))

if a==b or b==c or  c==a:
    print("sum is:",0)
else:
    print("sum is :",a+b+c)
