#!/usr/bin/python3
""" unitests """

import pep8
import unittest
import models.base
import models.rectangle
import models.square
import json

Base = models.base.Base
Rectangle = models.rectangle.Rectangle
Square = models.square.Square


class TestRectangle(unittest.TestCase):
    """ Class rectangle tests """
    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")
