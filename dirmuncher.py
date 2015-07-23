#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import os

class Dirmuncher:
    def __init__(self, directory):
        self.directory = directory

    def getFiles(self):
        result = {}

        for dirname, dirnames, filenames in os.walk(self.directory):
            # Subdirectories
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))

            # Filenames
            for filename in filenames:
                print(os.path.join(dirname, filename))

            result[dirname] = filenames

        return result


if __name__ == "__main__":
    muncher = Dirmuncher('movies')
    print(muncher.getFiles())
