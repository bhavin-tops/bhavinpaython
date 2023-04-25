#wite a python program to get the fibonacci series of given range.

n=int(input("enter the number:"))
x=0
y=1
z=0

while(z<=n):
    print(z,end=" ")
    x=y
    y=z
    z=x+y
