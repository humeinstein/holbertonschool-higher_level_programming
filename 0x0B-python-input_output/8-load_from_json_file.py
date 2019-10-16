#!/usr/bin/python3
"""
load_from_json func
"""

import json

def load_from_json_file(filename):
    """obj from jsonfile"""
    with open(filename, 'r', encoding='utf-8') as filec:
        return json.load(filec)