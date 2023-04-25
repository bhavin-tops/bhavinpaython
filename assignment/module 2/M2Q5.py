# what is the purpose continue statement in python?

'''continue keyword is used to end the current iteration
  in a for loop (or a while loop), and continue to the next
  iteration'''

#for example
for i in range(1,11):
    if i==6:
        continue
    print(i)
