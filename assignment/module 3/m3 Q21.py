# Write a Python program to convert a tuple to a string

def convert_tuple(c_tuple):  
  str=''  
  for i in c_tuple:  
    str=str+i  
  return str  
  
c_tuple=('A','D','I','T','Y','A',' ','P','A','T','E','L')  
c_string=convert_tuple(c_tuple)  
print(c_string) 
