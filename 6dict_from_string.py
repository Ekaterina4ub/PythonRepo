# The user enters a string.
# Print a dictionary where keys are even characters in the string and values are odd characters in the string.
# If the last key lacks a value, do not add it to the dictionary.
from pip._vendor.distlib.compat import raw_input

text = raw_input("Enter the string: ")

string_len = len(text)

for i in range(0, string_len, 2):
    if string_len % 2 != 0 and i == string_len - 1:
        break
    items = [(text[i + 1], text[i])]
    print(dict(items))
