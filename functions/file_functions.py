import magic
import os
from pathlib import Path

FILE_FUNCTIONS = dict()

def register(func):
    """Register a function that can be apply to Files"""
    FILE_FUNCTIONS[func.__name__] = func
    return func

@register
def file_type(file_path: str, file_type:str):
    """Inspects the type of the file using magic library"""
    def file_mime_type(filename):
        result = ""
        try:
            mime = magic.Magic(mime=True)
            result = mime.from_file(filename)
        except PermissionError:
            #print("Error on magic library")
            return result
        return result

    current_file_type = file_mime_type(file_path)
    if current_file_type == file_type:
        return True
    return False


@register
def file_owner(file_path:str, owner:str):
    """Passing a complete path to file, it checks the owner of the file"""
    try:
        current_owner = Path(file_path).owner()
    except KeyError as ex:
        # KeyError: 'getpwuid(): uid not found: For deleted users
        # print("User no more present in the system", ex)
        return False
    if current_owner == owner:
        return True
    return False

@register
def file_size(file_path:str, size:int):
    """ Passing an absolute file path, it checks the dimensions in KB    """
    try:
        current_size = os.stat(file_path).st_size
        if 0 < current_size < size:
            return True
    except FileNotFoundError as error:
        #print("Symbolic link points to a file not more present", error)
        return False

