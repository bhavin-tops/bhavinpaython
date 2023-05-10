# Write a Python function to get 
# the largest number, smallest num and 
# sum of all from a list

list = []
num = int(input('How many numbers:- '))
for n in range(num):
    numbers = int(input('Enter number :- '))
    list.append(numbers)
print("Maximum element in the list is :- ", max(list))
print("Minimum element in the list is :- ", min(list))
print("Sum of all list :- ",sum(list))
