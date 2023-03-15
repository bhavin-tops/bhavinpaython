#take  number input from user and find addition of all natural number upto the number

num=int(input("enter the num of addition:"))

def add(z):
    if z==0:
        return 0 
    else:
        return z+add(z-1)
print(f"addition of {num} is :",addition(num))

    
