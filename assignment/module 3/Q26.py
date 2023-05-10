#Write a Python program to replace last value of tuples in a list.

list1 = [(10,20,30),(40,50,60),(70,80,90),(100,110,120)]

print("Original List is : ",list1)
for i in list1:
    print(i[: -1] + (51,))          # last Index not printed and add 51 in last
