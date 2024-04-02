# Write a Python program to replace last value of tuples in a list

l = [(20, 30, 40), (50, 60, 60), (90, 10, 90)] # 40=100,60=100,90=100
print([t[:-1] + (100,) for t in l])
