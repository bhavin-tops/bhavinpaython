#wap that swap variable without using third variable

a=int(input("enter the number A:"))
b=int(input("enter thr number B:"))

a=a+b
b=a-b
a=a-b

print("after swapping A:",a)
print("after swapping B:",b)
