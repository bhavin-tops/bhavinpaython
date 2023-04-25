#write python program to test whether a passed letter is vowel  or not.

y=int(input("enter the sentance:"))
count=0

for  i in y :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
     print(i)
    count=count+1
if count==0:
    print("no vowel found:")
else:
    print("number of vowel:",count)
