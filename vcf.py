#!/usr/bin/env python
import re
import sys


class Vcf:
    def __init__(self, file, chromosomes=False):
        """

        :param file:
        :param chromosomes:
        """
        self.file = file
        if chromosomes:
            fill = "("
            if re.match(",", chromosomes):
                for number in chromosomes.split(","):
                    fill += number + "|"
                fill = fill[:-1]
            else:
                fill += chromosomes
            self.chromosome = fill + ")"  # chromosme numbers 1,2,4
        else:
            self.chromosome = "(\d+)"

    def deletion(self, size):
        """

        :param size:
        """
        file = open(self.file, "r")
        vcf_content = file.read()
        text = ""
        not_valid_vcf = True
        if vcf_content.startswith("##fileformat=VCFv4.0"):
            not_valid_vcf = False
            for x in re.findall("\n" + self.chromosome + "\t(\d+)\t.+\t([ATCG]+)\t([ATCG]+).+", vcf_content):
                if x[2].__len__() > x[3].__len__():
                    if (x[2].__len__() - x[3].__len__()) > size:
                        if "," not in x[-1]:
                            text += x[1] + "|" + str(int(x[1]) + x[2].__len__()) + "\n"
        if vcf_content.startswith("##fileformat=VCFv4.1"):
            not_valid_vcf = False
            for x in re.findall("\n" + self.chromosome + "\t(\d+)\t.+\<DEL\>.+END=(\d+).+", vcf_content):
                if (int(x[2]) - int(x[1])) > size:
                    text += x[1] + "|" + x[2] + "\n"
        if not_valid_vcf:
            raise TypeError(" vcf is not 4.0 or 4.1 ")
        self.v_c_f = text
        self.vcf_exists = True
        file.close()

    def read_vcf(self):
        """

        """
        if self.vcf_exists:
            self.intervals = [[int(number[0]), int(number[1])] for number in
                              [numbers.split("|") for numbers in self.v_c_f.split("\n")][:-1]]
        else:
            print("no vcf")
            sys.exit(0)


def main():
    print("no main")


if __name__ == "__main__":
    main()
