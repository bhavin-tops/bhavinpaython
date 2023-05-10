# Write a Python script to merge two Python dictionaries

dic_1 = {'name': 'Rachit', 'Roll no': 36, 'Marks': 29}
dic_2 = {'Name': 'Vishal', 'roll no': 53, 'marks': 22}

d = dic_1.copy()
d.update(dic_2)

print(d)
