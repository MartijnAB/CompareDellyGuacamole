#!/usr/bin/env python
import re


class Guacemole():

    def __init__(self, path):
        self.path = path

    def __load__(self):
        uikomstguacemoel = open(self.path, "r")
        self.guacemole = uikomstguacemoel.read()
        uikomstguacemoel.close()

    def lees_guacemole(self, size):
        self.intervals = []
        for GenomeRange in [[int(numbers.split(",")[0]), int(numbers.split(",")[1])] for numbers in re.findall("\d+,(\d+,\d+)", self.guacemole.split("List")[1])]:
            if GenomeRange[0] < GenomeRange[1]:
                if (int(GenomeRange[1]) - int(GenomeRange[0])) > size:
                    self.intervals += [GenomeRange]
            else:
                if (int(GenomeRange[0]) - int(GenomeRange[1])) > size:
                    self.intervals += [[GenomeRange[1], GenomeRange[0]]]


def main():
    print(" no main ")

if __name__ == "__main__":
    main()