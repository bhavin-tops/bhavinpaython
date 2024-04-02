# Write a Python program to convert a list of tuples into a dictionary

def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di


# Driver Code
tups = [("aditya", 7), ("kunal", 10), ("anand", 99)]

dictionary = {}
print(Convert(tups, dictionary))
