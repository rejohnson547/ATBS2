# 01/22/2020
#! python3
# This program adds Wikipedia bullet pints to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Seperate lines and add stars.

pyperclip.copy(text)