#Write a Python program to check multiple keys exists in a dictionary

dict={'a': 1, 'b': 2, 'c': 3, 'd': 4}
count=0
for i in dict:
    count+=1
if count==1:
    print("Only one key exists in dictionary")
elif count>1:
    print("Multiple key exists in dictionary")
else :
    print("Dictionary is empty")
