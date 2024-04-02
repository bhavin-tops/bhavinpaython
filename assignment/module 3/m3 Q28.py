# Write a Python program to remove an empty tuple(s) from a list of tuples

# Python program to remove empty tuples from s
# list of tuples function to remove empty tuples
# using list comprehension
def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

# Driver Code
tuples = [(), ('aditya','15','8'), (), ('ridham', 'anshu'),
		('bhavin', 'kunal', '45'), ('',''),()]
print(Remove(tuples))
