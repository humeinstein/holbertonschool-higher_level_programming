#!/usr/bin/python3
"""
function that prints a text with 2 new lines when . ? :
"""
def text_indentation(text):

    errorStatus = checkTypeError(text)
    if errorStatus == 1:
        raise TypeError("text must be a string")
    
    letter = 0
    while letter < len(text):
        print("{}".format(text[letter]), end="")
        if text[letter] == "." or text[letter] == "?" or text[letter] == ":":
            print()
            print()
            if letter == len(text) - 1:
                break
            if text[letter + 1] == " ":
                letter += 1
        letter += 1
        


"""
function that returns 0 for false 1 for true
"""
def checkTypeError(text):
    """
    return 1 if false
    """
    error = 0
    if type(text) is not str:
        error = 1
    return error