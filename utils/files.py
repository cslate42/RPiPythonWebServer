import os
# import config


def scan(path):
    """
    Walk through a path recursively and return a list
    Args:
        path (str): the path to scan
    Returns:
        list: the multi dimensional path list
    TODO populate items
    """
    items = []
    for root, directories, filenames in os.walk(path):
        for directory in directories:
            print os.path.join(root, directory)
        for filename in filenames:
            print os.path.join(root, filename)
    return items
