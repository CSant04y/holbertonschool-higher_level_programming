#!/usr/bin/python3
"""unittest for Base class"""


import unittest
import pep8
from models.base import Base


class Test_Base(unittest.TestCase):
    """[This Test the class Base]

    Args:
        unittest: [unitest module]
    """
    @classmethod
    def setUpClass(cls):
        """[This sets up the class for use]
        """
        cls.b1 = Base()
        cls.b2 = Base(50)
        cls.b3 = Base(-1)
        cls.b4 = Base(12)
        cls.b5 = Base()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5

    def test_instantation(self):
        """[This is where we test instatiation of id]
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 50)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 2)

    def test_to_json_string(self):
        """[This test the to json string file]
        """
        list_dict = [{'id': 8}, {'id': None}, {'id': 358}, {'id': -16}]
        self.assertEqual(Base.to_json_string(list_dict),
                         '[{"id": 8}, {"id": null}, {"id": 358}, {"id": -16}]')

    def test_pep8(self):
        """Automated testing of coding file using the pep8 coding style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
