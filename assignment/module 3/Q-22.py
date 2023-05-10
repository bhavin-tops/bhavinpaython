#Write a Python program to check whether an element exists within a tuple.


t = (12,9,10,13)

print("main tuple list is",t)

n = int(input("enter number:"))

if n in t:
    print(n,"exists in tuple")
else:
    print(n,"does not exist in tuple")
