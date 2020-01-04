# 01/03/2020

spam = ['apples', 'bananas', 'tofu', 'cats']
games = ['Pokemon Sword/Shield', 'Resident Evil 2', 'Call of Duty', 'Dragon Quest 11']


def comma_code(lst):
    new_list = lst
    last = new_list[-1]
    del new_list[-1]
    new_list.append('and')
    new_list.append(last)

    for item in new_list:
        print(item, end=' ')

comma_code(spam)
comma_code(games)