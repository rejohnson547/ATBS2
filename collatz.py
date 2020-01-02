# 12/30/2019

def collatz(number):
    if number % 2 == 0:
    	answer = number // 2
    	print(answer)
    elif number % 2 == 1:
    	answer = 3 * number + 1
    	print(answer)
    if answer != 1:
    	collatz(answer)


try:
	num = int(input('Please enter a number: '))
except ValueError:
	print('You did not enter a number:')
	collatz(num)
 
collatz(num)
