from functions import py_one
from unittest import TestCase
import array as arr

#A function that given 2 vectors of integers finds the first repeated number

class PyOneTest(TestCase):

    def test_result(self):
        vector1 = arr.array('I', [1, 2, 3, 1])
        vector2 = arr.array('I', [19, 4, 2])
        assert py_one.findFirstRepeated(vector1, vector2) == 2

    def test_two(self):
        vector1 = arr.array('I', [1, 2, 3, 1, 1, 2, 3, 1])
        vector2 = arr.array('I', [1, 2, 3, 1])
        assert py_one.findFirstRepeated(vector1, vector2) == 1


    def test_three(self):
        vector1 = arr.array('I', [1, 2, 3, 1, 1, 2, 3, 1])
        vector2 = arr.array('I', [1, 2, 3, 1])
        assert py_one.findFirstRepeated(vector2, vector1) == 1

    def test_empty(self):
        vector1 = arr.array('I', [])
        vector2 = arr.array('I', [1, 2, 3, 1])
        assert py_one.findFirstRepeated(vector2, vector1) == None

    def test_empty2(self):
        vector1 = arr.array('I', [])
        vector2 = arr.array('I', [])
        assert py_one.findFirstRepeated(vector2, vector1) == None