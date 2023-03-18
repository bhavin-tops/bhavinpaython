# WAP function to reverses a string if its length is multiple of 4 

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('axyz'))
print(reverse_string('python'))
