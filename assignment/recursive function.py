#recursive function:

num=int(input("enter num to find  factorial:"))
def factorial(x):
     if x<=0:
         return 1
     else:
      return x*factorial(x-1)

print(f"factorial of{num}is:",factorial(num))
