#!/usr/bin/python3
"""me and steve testing why im not getting checks"""

import pep8
import unittest
import models.base
import models.rectangle

Rectangle = models.rectangle.Rectangle
Base = models.base.Base


class RectangleTest(unittest.TestCase):
    """Test cases for rectangle"""

    def setUp(self):
        """set assertEquals to ae"""

        self.ae = self.assertEqual

    @classmethod
    def tearDownClass(cls):
        """tear down class"""

        pass

    def test_value_rect(self):
        """test normal values"""

        r1 = Rectangle(1, 2, 3, 4)

        self.ae(r1.width, 1)
        self.ae(r1.height, 2)
        self.ae(r1.x, 3)
        self.ae(r1.y, 4)
