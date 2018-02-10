import os
import config


def scan(path):
    items = []
    for root, directories, filenames in os.walk(path):
        for directory in directories:
            print os.path.join(root, directory)
        for filename in filenames:
            print os.path.join(root, filename)
    return items
