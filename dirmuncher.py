#!/usr/bin/env python
# -*- Coding: utf-8 -*-

import os
import enchant

class Dirmuncher:
    delimeters = ['.', ' ']

    def __init__(self, directory):
        self.directory = directory
        self.dictionary = enchant.Dict("en_US")

    def getFiles(self):
        result = {}

        for dirname, dirnames, filenames in os.walk(self.directory):
            # Get subdirectories
            # for subdirname in dirnames:
            #     print(os.path.join(dirname, subdirname))

            # Get filenames
            # for filename in filenames:
            #     print(os.path.join(dirname, filename))

            result[dirname] = filenames

        return result

    def process(self, filename):
        name = []

        for delimeter in self.delimeters:
            for word in filename.split(delimeter):
                if self.lookup(word):
                    name.append(word)

        return name

    def lookup(self, word):
        return self.dictionary.check(word)


if __name__ == "__main__":
    muncher = Dirmuncher('movies')

    terms = muncher.getFiles()

    for directory, filenames in terms.items():
        for filename in filenames:
            print(muncher.process(filename))
