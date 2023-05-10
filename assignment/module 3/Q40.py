#Write a Python program to map two lists into a dictionary

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
d={}
for key in l1:
    for value in l2:
        d[key]=value
        l2.remove(value)
        break
print(d)
