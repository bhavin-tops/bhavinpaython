#wap electricity bill total & avg

month1=int(input("enter the first month bill :"))
month2=int(input("enter the second month bill :"))
month3=int(input("enter the third month bill :"))

total=(month1+month2+month3)
avg=(month1+month2+month3)/3

print("total electricity bill:",total)
print("avg electricity bill:",avg)
