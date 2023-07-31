#make sure specific student can only search by id - any appropriate validation if
#user entered wrong input - if id doesn’t fetch data from dictionary display user
#does not exist
import re

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Define a function for
# for validating an Email
def check(email):

	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = "ankitkp326@gmail.com"

	# calling run function
	check(email)

	email = "keyurshah452@gmail.com"
	check(email)

	email = "ankitkp326.com"
	check(email)
