#!/usr/bin/python3

""" unitests """

import unittest
from models.base import Base



class Testbase_create(unittest.TestCase):
    """ test creation """
    def testforstring(self):
        self.assertEqual("wow", Base("wow").id)
        
    def argumentss(self):
        test = Base()
        test2 = Base()
        self.assertEqual(test.id, test2.id - 1)
