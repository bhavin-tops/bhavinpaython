#function with arbitary parameter(*args)

def add(*args):
    sum=0
    for i in args:
        sum+=i
        return sum
print("addition of tuple values:",add(12,34,56))
