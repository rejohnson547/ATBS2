# 01/22/2020
#! python3
# This program adds Wikipedia bullet pints to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')

for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '*' + lines[i] # add star to each string in "lines" list

text = '\n'.join(lines)


pyperclip.copy(text)