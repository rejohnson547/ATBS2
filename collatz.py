# 12/30/2019

number = int(input('Please enter a number: '))

def collatz(number):
    while True:
        if number % 2 == 0:
            return number // 2
        elif number % 2 == 1:
            return 3 * number + 1
    
print(collatz(number))