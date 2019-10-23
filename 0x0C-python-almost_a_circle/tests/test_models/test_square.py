#!/usr/bin/python3

""" unitests """

import unittest
from models.square import Square
import pep8

def test_pep8_conformance(self):
        """test that we conform to pep8"""

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["square.py"])
        self.ae(result.total_errors, 0,
                "Found code style errors (and warnings).")
