#!/usr/bin/python3
"""
function writes string to txt
"""

def write_file(filename="", text=""):
    """writes string to txtfile"""
    with open(filename, mode='w', encoding="utf-8") as filec:
        written = filec.write(text)
    return written