# Write a Python program to unzip a list of tuples into individual lists

#create a tuple
l = [(1,'a'), (2,'b'), (3,'c')]
print(list(zip(*l)))
