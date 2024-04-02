# How will you remove last object from a list? 

''' The del operator deletes the element at the specified index location
     from the list. To delete the last element, 
        we can use the negative index  -1. The use 
    of the negative index allows us to delete the last element,
   even without calculating the length of the list'''


list = [2,33,222,14,25]
print("Original list: " ,str(list))

# call del operator
del list[-1]           # remove 25

# print the updated list
print("Updated list: " ,str(list))
