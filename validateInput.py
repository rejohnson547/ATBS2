#01/17/2020

while True:
	print('Enter your age: ')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')


while True:
	print('Select a new password (letters and numbers only):')
	password = input()
	if password.isalnum():
		break
	print('Passwords can only be letters and numbers.')
