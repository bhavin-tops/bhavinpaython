#Write a Python program to print all unique values in a dictionary. 
L = [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
list=[]
for i in L:
    for dic in i.values():
        list.append(dic)
print(set(list))
