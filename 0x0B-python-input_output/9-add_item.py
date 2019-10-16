#!/usr/bin/python3
"""
adds all arguments file
"""

from sys import argv
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filen = "add_item.json"

try:
    jsonl = load_from_json_file(filen)
except:
    jsonl = []

for arg in argv[1:]:
    jsonl.append(arg)
save_to_json_file(jsonl, filen)