#convert list to tuple without using tuple() function
list=[1,2,3,4,5,6,7,8,9]
tuple=()
for i in list:
    tuple=tuple+ (i,)

print(tuple)
