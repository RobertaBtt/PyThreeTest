from functions import py_two
from unittest import TestCase
import pathlib

class PyTwoTest(TestCase):

    def test_result_current_dir(self):

        path = pathlib.Path().absolute()
        file_type = "text/plain"
        file_owner = "root"
        file_size = 14 * 2 ** 20

        data = {
            'file_type': file_type,
            'file_owner': file_owner,
            'file_size': file_size
        }
        assert py_two.findFirstFile(path, data) == "Not Found"

    def test_result_root_executable(self):

        path = pathlib.Path().absolute()

        file_type = "application/x-executable"
        file_owner = "root"
        file_size = 14 * 2 ** 20

        data = {
            'file_type': file_type,
            'file_owner': file_owner,
            'file_size': file_size
        }
        assert "github/PyThreeTest/busybox" in py_two.findFirstFile(path, data)

