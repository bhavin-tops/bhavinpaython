#wap that swap variable without using third variable

a=int(input("enter the number A:"))
b=int(input("enter the number B:"))

a=a+b
b=a-b
a=a-b

print("after swaping a:",a)
print("after swaping b:",b)
