#!/usr/bin/env python
import argparse
import sys
import compareDeleties
import vcf
import guacemole


"""
This program “CompareDellyGuacamole” takes the position of reported deletions (of a minimum length)
in a v.c.f. or Guacamole file en compares them.  One file is the reference for the oder, the alternative.

A deletion in the reference that is not in alternative is reported as “missed”,
A deletion in the alternative that is not in reference is reported as “false positive”.
A true positive is a reported deletion in the alternative that shares a minimum of one base pair
whit a reported deletion in the reference.

The out put consist of de number of: missed, true positives, false positives, multiple true positives,
end the number of deletions in the reference en in the alternative.


Author: Martijn A B

4-1-2016
"""


class Pars:
    """This class provide everything needed to pars arguments from a user."""

    def __init__(self):
        """The definition of the default of some arguments."""

        self.rtyp = "vcf"
        self.atyp = "vcf"
        self.size_del = 300
        self.out = "out"
        self.writing = "other"

    def load_arguments(self):
        """load_arguments get the arguments of the user en perform some checks."""

        parser = argparse.ArgumentParser(description='alt vs ref')
        parser.add_argument('-alt', type=str, help='alt vcf or out guacemole.')
        parser.add_argument('-ref', type=str, help='ref vcf or out guacemole.')
        parser.add_argument('-atyp', type=str, help='Typ alt. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-rtyp', type=str, help='Typ ref. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-size', type=int, help='The min size of a deletion.\tdefault = 300')
        parser.add_argument('-out', type=str, help='Pat output.\tdefault = "out"')
        parser.add_argument('-printen', type=str, help='Pat output.\tdefault = "out"')
        parser.add_argument('-writing', type=str, help='"none" for no output "all" for all the coordinate '
                                                       'FP, TP, FN, TN et cetera etcetera et cetera etcetera.')
        args = parser.parse_args()
        """the variable become the input or default"""
        if args.alt is None or args.ref is None:
            print("You must specify an -alt and -ref otherwise the program stops.\nuse -h for help")
            sys.exit()
        self.alt = args.alt  # The definition of “self” not in the __init__ is to insure the definition of valid input
        self.ref = args.ref  # The definition of “self” not in the __init__ is to insure the definition of valid input
        if args.rtyp is not None:
            rtyp = args.rtyp.lower()
            if rtyp == "vcf" or rtyp == "guacemole":
                self.rtyp = rtyp
            else:
                print('rtpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.atyp is not None:
            atyp = args.atyp.lower()
            if atyp == "vcf" or atyp == "guacemole":
                self.atyp = atyp
            else:
                print('atpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.size is not None:
            self.size_del = args.size
        if args.out is not None:
            self.out = args.out
        if args.writing is not None:
            self.writing = args.writing.lower()


def output_file(comparing, pat, all):
    """Write the result in a file en if “all” is True, than the data is also given.
    :param comparing: A object of type compareDeleties containing the results.
    :param pat: A string containing the pat of the output file.
    :param all: A boolean that if true leads to the printing of the intervals linked to the reported statistics.
    """

    writ = open(pat, "w")
    writ.write("missed " + str(comparing.missed.__len__()) + "\n")
    writ.write("true positives " + str(comparing.true_positives.__len__()) + "\n")
    writ.write("false positives " + str(comparing.false_positives.__len__()) + "\n")
    writ.write("multiple true positives " + str(comparing.multiple_true_positives.__len__()) + "\n")
    writ.write("number of intervals alt " + str(comparing.alt.intervals.__len__()) + "\n")
    writ.write("number of intervals ref " + str(comparing.ref.intervals.__len__()) + "\n")
    if all:
        writ.write("missed " + str(comparing.missed) + "\n")
        writ.write("true positives " + str(comparing.true_positives) + "\n")
        writ.write("false positives " + str(comparing.false_positives) + "\n")
        writ.write("multiple true positives " + str(comparing.multiple_true_positives) + "\n")
    writ.close()


def make_vcf(alt_ref, size_del):
    """Provide information from a v.c.f. file as a Vcf class.
    :param alt_ref: A string of the pat of the v.c.f. file that contains the reference or the alternative.
    :param size_del: A int containing the minimum length of a deletion to be reported as a deletion.
    :return: A object of type Vcf containing the necessary information.
    """

    run_vcf = vcf.Vcf(alt_ref)
    try:
        run_vcf.deletion(size_del)
    except TypeError or IndexError:
        print("your vcf file does not meet the required -h for help")
        sys.exit(1)
    run_vcf.read_vcf()
    return run_vcf


def make_guacemole(alt_ref, size_del):
    """Provide information from a guacemole file as a Guacemole class.
    :param alt_ref: A string of the pat of the guacemole file that contains the reference or the alternative.
    :param size_del: A int containing the minimum length of a deletion to be reported as a deletion.
    :return: A object of type Guacemole containing the necessary information.
    """

    run_guacemole = guacemole.Guacemole(alt_ref)
    run_guacemole.__load__()
    try:
        run_guacemole.read_guacemole(size_del)
    except IndexError:
        print("your guacemole file does not meet the required -h for help")
        sys.exit(1)
    return run_guacemole


def main():
    """Runs the program."""
    run = Pars()
    run.load_arguments()
    run_comparing = compareDeleties.Compare()
    print("start program CompareDellyGuacamole\n")
    """Depending on the input is decided how to read the files."""
    if run.atyp == run.rtyp:
        if run.atyp == "vcf":
            run_alt = make_vcf(run.alt, run.size_del)
            run_ref = make_vcf(run.ref, run.size_del)
        else:
            run_alt = make_guacemole(run.alt, run.size_del)
            run_ref = make_guacemole(run.ref, run.size_del)
    else:
        if run.atyp == "vcf":
            run_alt = make_vcf(run.alt, run.size_del)
            run_ref = make_guacemole(run.ref, run.size_del)
        else:
            run_alt = make_guacemole(run.alt, run.size_del)
            run_ref = make_vcf(run.ref, run.size_del)
    run_comparing.__init__(run_alt, run_ref)
    run_comparing.overlap()
    """Generate output file or not?"""
    if run.writing != "none":
        if run.writing == "all":
            output_file(run_comparing, run.out, True)
        else:
            output_file(run_comparing, run.out, False)
    print("\nprogram finished")


if __name__ == '__main__':
    main()
