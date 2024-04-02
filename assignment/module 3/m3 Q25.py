# Write a Python program to reverse a tuple

# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
	
# Driver Code
tuples = ('A','D','I','T','Y','A')
print(Reverse(tuples))
