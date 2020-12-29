from functions import py_one
from unittest import TestCase
import array as arr


class PyOneTest(TestCase):
    def setUp(self):
        self.vector1 = arr.array('I',[1,2,3,1])
        self.vector2 = arr.array('I',[19,4,2])

    def test_result(self):
         assert py_one.findFirstRepeated(self.vector1, self.vector2) == 2