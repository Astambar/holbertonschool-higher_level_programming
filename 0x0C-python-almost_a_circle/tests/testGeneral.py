#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import unittest
sys.path.append('../')

from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Square(self):

        square1 = Square(5)
        self.assertEqual(square1.id, 1)
        self.assertEqual(square1.y, 0)
        self.assertEqual(square1.x, 0)
        self.assertEqual(square1.size, 5)

        square2 = Square(3,4,3)
        self.assertEqual(square2.id, 2)
        self.assertEqual(square2.y, 3)
        self.assertEqual(square2.x, 4)
        self.assertEqual(square2.size, 3)

        square3 = Square(3,4,3,5)
        self.assertEqual(square3.id, 5)
        self.assertEqual(square3.y, 3)
        self.assertEqual(square3.x, 4)
        self.assertEqual(square3.size, 3)
    

if __name__ == '__main__':
    unittest.main()