from functions import py_three
from unittest import TestCase


class PyThirdTest(TestCase):

    def test_example(self):
         assert py_three.countChangeCoinInterval('0110') == 2

    def test_result(self):
         assert py_three.countChangeCoinInterval('111110') == 2

    def test_result_three(self):
         assert py_three.countChangeCoinInterval('01101011') == 3


    def test_four(self):
         assert py_three.countChangeCoinInterval('1') == 0

    def test_empty(self):
         assert py_three.countChangeCoinInterval('') is None

    def test_raise(self):
        with self.assertRaises(ValueError):
            result = py_three.countChangeCoinInterval('not valid')
