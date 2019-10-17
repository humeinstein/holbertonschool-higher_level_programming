#!/usr/bin/python3
"""add_attrri"""


def add_attribute(obj, name, value):
    """add new attr"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')