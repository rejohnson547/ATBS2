# 12/30/2019

number = int(input('Please enter a number: '))

def collatz(number):
    while True:
        if number % 2 == 0:
            answer = number // 2
            print(answer)
        elif number % 2 == 1:
            answer = 3 * number + 1
            print(answer)
        elif answer != 1:
            collatz(answer)
        else:
            break

        
print(collatz(number))