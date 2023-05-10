# Write a Python program to remove an empty tuple(s) from a list of tuples. 

my_tuple = [(),("x","y"),("a","b","c",9),(),(11,12,13,14),()]

#Function for Remove Empty tuple from list of tuples
def remove_tuple(my_tuple):
    for i in my_tuple:
        if len(i) == 0:
            my_tuple.remove(i)
    return my_tuple

print(remove_tuple(my_tuple))
