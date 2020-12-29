from functions import py_three
from unittest import TestCase
from array import array as arr

class PyThirdTest(TestCase):

    def setUp(self):
        # h for unsigned short
        self.coins = arr.array('h',[0,1,0,1])

    def test_result(self):
         assert py_three.countChangeCoinInterval(self.coins) == 2



