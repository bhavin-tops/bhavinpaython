# Differentiate between append () and extend () methods? 

'''The append() method in the programming language Python adds an item to a list     
      that already exists whereas the extend() method adds each of 
        the iterable element which is supplied as a parameter to the 
    end of the original list
'''

# extend

a=[1,2,3]
b=[1,2,3,4,5]
a.extend([4,5])
b.append([6,7,8,9,10])

print("Extend :- ",a)
print("Append :- ",b)
