# 01/27/2020

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    else:
        return True

print('Is 415-555-4242 a phone number?')
print(is_phone_number('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(is_phone_number('Moshi moshi'))