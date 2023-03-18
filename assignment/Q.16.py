# write a python program  to get a single strin from two given strings,
# separated by a space and swap the first two characters of each strings

str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")

x=str1[0:2]

str1=str1.replace(str1[0:2],str2[0:2])

str2=str2.replace(str2[0:2],x)

print("Your second string has become :- ",str2)
print("Your first string has become :- ",str1)


