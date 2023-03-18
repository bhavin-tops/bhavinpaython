# write a python program to count the number of characters (character frequency ) in astring

n=input("Enter the String: ").lower()
z={}
for i in n:
    if i in z:
        z[i]+=1 
    else:
        z[i]=1
print(z)
