import argparse
import sys
import vergelijkDeleties
import vcf
import guacemole


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
        parser.add_argument('-printen', type=str, help='Pat output.\tdefault = "out"')
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
                self.atyp = atyp
            else:
                print('atpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.size is not None:
            self.sizeDel = args.size
        if args.out is not None:
            self.out = args.out
        if args.writing is not None:
            self.writing = args.writing.lower()


def output_file(vergelijk, pat, all):
    writ = open(pat, "w")
    writ.write("missed " + str(vergelijk.missed.__len__()) + "\n")
    writ.write("true_positives " + str(vergelijk.true_positives.__len__()) + "\n")
    writ.write("false_positives " + str(vergelijk.false_positives.__len__()) + "\n")
    writ.write("multiple_true_positives " + str(vergelijk.multiple_true_positives.__len__()) + "\n")
    writ.write("number of intervals alt " + str(vergelijk.alt.intervals.__len__()) + "\n")
    writ.write("number of intervals ref " + str(vergelijk.ref.intervals.__len__()) + "\n")
    if all:
        writ.write("missed " + str(vergelijk.missed) + "\n")
        writ.write("true_positives " + str(vergelijk.true_positives) + "\n")
        writ.write("false_positives " + str(vergelijk.false_positives) + "\n")
        writ.write("multiple_true_positives " + str(vergelijk.multiple_true_positives) + "\n")
    writ.close()


def make_vcf(alt_ref, sizeDel):
    run_vcf = vcf.Vcf(alt_ref)
    run_vcf.deletion(sizeDel)
    # TODO: kontroleer of het een vcf is
    run_vcf.lees_vcf()
    return run_vcf


def make_guacemole(alt_ref, sizeDel):
    run_guacemole = guacemole.Guacemole(alt_ref)
    run_guacemole.__load__()
    try:
        run_guacemole.lees_guacemole(sizeDel)
    except IndexError:
        print("your guacemole file does not meet the required -h for help")
        sys.exit(1)
    return run_guacemole


def main():
    run = Pars()
    run.load_arguments()
    run_verglijk = vergelijkDeleties.Vergelijk()
    print("start")
    print(run.atyp + " alt type "+ run.rtyp + " ref type ")
    if run.atyp == run.rtyp:
        print(" typ ==")
        if run.atyp == "vcf":
            print("typ vcf")
            run_alt = make_vcf(run.alt, run.sizeDel)
            run_ref = make_vcf(run.ref, run.sizeDel)
        else:
            print('typ else')
            run_alt = make_guacemole(run.alt, run.sizeDel)
            run_ref = make_guacemole(run.ref, run.sizeDel)
    else:
        print(" typ !=")
        if run.atyp == "vcf":
            print("typ vcf")
            run_alt = make_vcf(run.alt, run.sizeDel)
            run_ref = make_guacemole(run.ref, run.sizeDel)
        else:
            print('typ else')
            run_alt = make_guacemole(run.alt, run.sizeDel)
            run_ref = make_vcf(run.ref, run.sizeDel)
    run_verglijk.__laden__(run_alt, run_ref)
    run_verglijk.overlap()

    if run.writing != "none":
        if run.writing == "all":
            output_file(run_verglijk, run.out, True)
        else:
            output_file(run_verglijk, run.out, False)


if __name__ == '__main__':
    main()
