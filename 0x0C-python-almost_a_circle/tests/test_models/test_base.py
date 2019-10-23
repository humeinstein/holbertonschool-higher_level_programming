#!/usr/bin/python3

""" unitests """

import pep8
import unittest
import models.base
import models.rectangle
import models.square
import json


def test_pep8_conformance(self):
    """test that we conform to pep8"""


<< << << < HEAD
pep8style = pep8.StyleGuide(quiet=True)
result = pep8style.check_files(["models/base.py"])
self.ae(result.total_errors, 0,
        "Found code style errors (and warnings).")
== == == =
pep8style = pep8.StyleGuide(quiet=True)
result = pep8style.check_files(["base.py"])
self.ae(result.total_errors, 0,
        "Found code style errors (and warnings).")
>>>>>> > df48d0280f006208ed6774d622b05776cce74bf3
