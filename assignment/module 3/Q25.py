# Write a Python program to reverse a tuple. 

tup = (1,2,3,4,5,6)

tup = list(tup)                              #convert tuple into list because tupleis immutable 
tup.reverse()

print(tuple(tup))
