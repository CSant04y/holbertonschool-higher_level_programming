#!/usr/bin/python3
"""unittest for Square class"""


import unittest
import pep8
from models.square import Square


class Test_Square(unittest.TestCase):
    """[This Test the class Square]

    Args:
        unittest: [unitest module]
    """
    @classmethod
    def setUpClass(cls):
        """[This sets up the class for use]
        """
        cls.s1 = Square(10)
        cls.s2 = Square(6, 66, 81)
        cls.s3 = Square(50)
        cls.s5 = Square(24, 86, 32, 62, )

    @classmethod
    def tearDownClass(cls):
        del cls.s1
        del cls.s2
        del cls.s3

    def test_sqr_instantation(self):
        """[This is where we test instatiation of id]
        """
        self.assertEqual(self.s1.id, 6)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.id, 7)
        self.assertEqual(self.s2.width, 6)
        self.assertEqual(self.s2.height, 6)
        self.assertEqual(self.s2.x, 66)
        self.assertEqual(self.s2.y, 81)
        self.assertEqual(self.s3.id, 8)
        self.assertEqual(self.s3.width, 50)
        self.assertEqual(self.s3.height, 50)
        self.assertEqual(self.s3.x, 0)
        self.assertEqual(self.s3.y, 0)

    def test_pep8(self):
        """Automated testing of coding file using the pep8 coding style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
