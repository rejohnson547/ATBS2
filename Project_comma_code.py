# 01/03/2020

"""Comma Code

Say you have a list value like this:

 spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and
a space, with and inserted before the last item. For example,
passing the previous spam list to the function would return 'apples,
bananas, tofu, and cats'. But your function should be able to work with any
list value passed to it."""

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