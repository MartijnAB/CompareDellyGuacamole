import argparse
import sys
import vergelijkDeleties_vcf_vcf
import verlglijkDeletsie_vcf_guacemole
import vergelijkDeleties_guacemole_guacemole


class Pars:
    def __init__(self):
        print("start programa")
        self.rtyp = "vcf"
        self.atyp = "vcf"
        self.sizeDel = 300
        self.out = "out"
        self.writing = "other"

    def load_arguments(self):
        parser = argparse.ArgumentParser(description='alt vs ref')
        parser.add_argument('-alt', type=str, help='alt vcf or out guacemole.')
        parser.add_argument('-ref', type=str, help='ref vcf or out guacemole.')
        parser.add_argument('-atyp', type=str, help='Typ alt. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-rtyp', type=str, help='Typ ref. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-size', type=int, help='The min size of a deletion.\tdefault = 300')
        parser.add_argument('-out', type=str, help='Pat output.\tdefault = "out"')
        parser.add_argument('-writing', type=str, help='"none" for no output "all" for all the coordinate '
                                                       'FP, TP, FN, TN et cetera etcetera et cetera etcetera.')
        args = parser.parse_args()
        if args.alt is None or args.ref is None:
            print("You must specify an -alt and -ref otherwise the program stops.\nuse -h for help")
            sys.exit()
        self.alt = args.alt
        self.ref = args.ref
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
                self.atyp = rtyp
            else:
                print('atpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.size is not None:
            self.sizeDel = args.size
        if args.out is not None:
            self.out = args.out
        if args.writing is not None:
            self.writing = args.writing.lower()


def outputFile(vergelijk, pat, all):
    writ = open(pat, "w")
    writ.write("missed " + str(vergelijk.missed.__len__()) + "\n")
    writ.write("true_positives " + str(vergelijk.true_positives.__len__()) + "\n")
    writ.write("false_positives " + str(vergelijk.false_positives.__len__()) + "\n")
    writ.write("multiple_true_positives " + str(vergelijk.multiple_true_positives.__len__()) + "\n")
    writ.write("number of intervals alt " + str(vergelijk.guacemole.intervals_.__len__()) + "\n")
    writ.write("number of intervals ref " + str(vergelijk.vcf.intervals_vcf.__len__()) + "\n")
    if all:
        writ.write("missed " + str(vergelijk.missed) + "\n")
        writ.write("true_positives " + str(vergelijk.true_positives) + "\n")
        writ.write("false_positives " + str(vergelijk.false_positives) + "\n")
        writ.write("multiple_true_positives " + str(vergelijk.multiple_true_positives) + "\n")
    writ.close()


def main():
    run = Pars()
    run.load_arguments()

    if run.atyp == run.rtyp:
        if run.atyp == "vcf":
            runVerglijk = vergelijkDeleties_vcf_vcf.Vergelijk()
            runVerglijk.__laden__(run.sizeDel, run.alt, run.ref)
        else:
            runVerglijk = vergelijkDeleties_guacemole_guacemole.Vergelijk()
            runVerglijk.__laden__(run.sizeDel, run.alt, run.ref)
        runVerglijk.overlap()
    else:
        runVerglijk = verlglijkDeletsie_vcf_guacemole.Vergelijk()
        if run.atyp == "vcf":
            runVerglijk.__laden__(run.sizeDel, run.alt, run.ref)
        else:
            runVerglijk.__laden__(run.sizeDel, run.ref, run.alt)
        runVerglijk.overlap()

    if run.writing != "none":
        if run.writing == "all":
            outputFile(runVerglijk, run.out, True)
        else:
            outputFile(runVerglijk, run.out, False)


if __name__ == '__main__':
    main()
