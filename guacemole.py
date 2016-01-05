#!/usr/bin/env python
import re


class Guacemole:
    """This class provide everything needed to get the deletions of a guacemole file."""

    def __init__(self, path):
        """
        :param path: A string containing the path to the guacemole file.
        """

        self.path = path

    def __load__(self):
        """Read the guacemole file."""

        info_guacemole = open(self.path, "r")
        self.guacemole = info_guacemole.read()
        info_guacemole.close()

    def read_guacemole(self, size):
        """Find the deletions in the guacemole file, end store the deletions in a variable.
        :param size: A int containing the minimum length of a deletion to be reported as a deletion.
        """

        intervals = []
        for GenomeRange in [[int(numbers.split(",")[0]), int(numbers.split(",")[1])] for numbers in re.findall("\d+,(\d+,\d+)", self.guacemole.split("List")[1])]:
            if GenomeRange[0] < GenomeRange[1]:
                if (int(GenomeRange[1]) - int(GenomeRange[0])) > size:
                    intervals += [GenomeRange]
            else:
                if (int(GenomeRange[0]) - int(GenomeRange[1])) > size:
                    intervals += [[GenomeRange[1], GenomeRange[0]]]

        """This "self" is not created in the __init__ to insure that it is created by this function.
        That is also the reason of this double definition.
        """
        self.intervals = intervals


def main():
    print(" no main ")

if __name__ == "__main__":
    main()