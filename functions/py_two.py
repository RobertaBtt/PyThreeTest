import os
from . import file_functions
not_found = "Not Found"


def findFirstFile(path: str, dictionary_properties: dict ):
    """According to the dictionary, returns the path of the
    file if all the conditions are satisfied."""
    for root, subdirs, files in os.walk(path):
        if len(files) > 0:
            for file in files:
                file_path = os.path.join(root, file)
                print("******",file_path)
                size = file_functions.FILE_FUNCTIONS['file_size'](file_path, dictionary_properties['file_size'])
                owner = file_functions.FILE_FUNCTIONS['file_owner'](file_path, dictionary_properties['file_owner'])
                type = file_functions.FILE_FUNCTIONS['file_type'](file_path, dictionary_properties['file_type'])

                if size and owner and type:
                    return file_path

    return not_found
