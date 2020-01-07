#!/usr/bin/python3
""" finds the peak """


def find_peak(list_of_integers):
    """finds peak"""
    if list_of_integers == []:
        return (None)
    else:
        return(max(list_of_integers))
