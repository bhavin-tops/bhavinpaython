# Write a Python program to find the length of a tuple.

# Define tuple
my_tuple = (1,9,45,36,"Python",True,9.6,5,"Hello")
print(len(my_tuple))  # Use Inbuilt function for find length of tuple


count = 0    # Initialize count to 0
# Use Loop for find length of a tuple
for i in my_tuple:
    count = count + 1
print("The Length of tuple is : ",count)
