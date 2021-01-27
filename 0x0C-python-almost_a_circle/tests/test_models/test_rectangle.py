#!/usr/bin/python3
"""unittest for Rectangle class class"""


import unittest
import pep8
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """[This Test the class Rectangle class that inherits from base]

    Args:
        unittest: [unitest module]
    """
    @classmethod
    def setUpClass(cls):
        """[This sets up the class for use with at least two values]
        """
        cls.r1 = Rectangle(11, 2)
        cls.r2 = Rectangle(5, 67, 55, 81)
        cls.r3 = Rectangle(22, 88, 42, 15, 74)
        cls.r4 = Rectangle(60, 200)

    @classmethod
    def tearDownClass(cls):
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4

    def test_rect_instantation(self):
        """[This is where we test instatiation of id]
        """
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.width, 11)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r2.height, 67)
        self.assertEqual(self.r2.x, 55)
        self.assertEqual(self.r2.y, 81)

        self.assertEqual(self.r3.id, 74)
        self.assertEqual(self.r3.width, 22)
        self.assertEqual(self.r3.height, 88)
        self.assertEqual(self.r3.x, 42)
        self.assertEqual(self.r3.y, 15)

        self.assertEqual(self.r4.id, 5)
        self.assertEqual(self.r4.width, 60)
        self.assertEqual(self.r4.height, 200)
        self.assertEqual(self.r4.x, 0)
        self.assertEqual(self.r4.y, 0)

    def test_errors(self):
        """[This fucntion test know cases that cause failure when initilized]
        """
        self.assertRaises(TypeError, self.r1.__init__, ["6", "5"])
        self.assertRaises(TypeError, self.r1.__init__, [[8], [2]])
        self.assertRaises(TypeError, self.r1.__init__, [3.75659, 3.14186])
        self.assertRaises(TypeError, self.r1.__init__, [{7}, {13}])
        self.assertRaises(TypeError, self.r1.__init__, [(5,), (56,)])
        self.assertRaises(TypeError, self.r1.__init__, [None, None])
#        self.assertRaises(ValueError, self.r1.__init__, [7, -15])

    def test_pep8(self):
        """Automated testing of coding file using the pep8 coding style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
