from functions import py_two
from unittest import TestCase


class PyTwoTest(TestCase):

    def setUp(self):
        self.path = "\\home\\user"

    def test_result(self):
         assert py_two.checkFileProperties(self.path) == "script.sh"

