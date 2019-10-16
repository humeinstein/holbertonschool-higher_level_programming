#!/usr/bin/python3
"""
save object 2 file
"""

import json

def save_to_json_file(my_obj, filename):
    """save file"""
    with open(filename, mode='w') as filec:
        filec.write(json.dumps(my_obj))