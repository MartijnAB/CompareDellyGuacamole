import argparse

import sys


class Pars:
    def __init__(self):
        print("start programa")
        self.rtyp = "vcf"
        self.atyp = "vcf"
        self.sizeDel = 300
        self.out = ""

    def load_arguments(self):
        parser = argparse.ArgumentParser(description='alt vs ref')
        parser.add_argument('-alt', type=str, help='als vcf or out guacemole.')
        parser.add_argument('-ref', type=str, help='ref vcf or out guacemole.')
        parser.add_argument('-atyp', type=str, help='Typ alt. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-rtyp', type=str, help='Typ ref. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-del', type=int, help='The min size of a deletion.')
        parser.add_argument('-out', type=str, help='Pat output.\tdefault = ""')
        args = parser.parse_args()
        if args.alt is None or args.ref is None:
            print("You must specify an -alt and -ref otherwise the program stops.\nuse -h for help")
            sys.exit()
        self.alt = args.alt
        self.ref = args.ref
        if args.rtyp is not None:
            rtyp = args.rtyp.lower()
            if rtyp == "vcf" or rtyp == "guacemole":
                self.rtyp = args.rtyp
            else:
                print('rtpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.atyp is not None:
            atyp = args.atyp
            if atyp == "vcf" or atyp == "guacemole":
                self.atyp = args.rtyp
            else:
                print('atpy must be vcf or guacemole.\nuse -h for help')
                sys.exit()
        if args.size is not None:
            self.sizeDel = args.size
        if args.out is not None:
            self.out = args.out


def main():
    run = Pars()
    run.load_arguments()


if __name__ == '__main__':
    main()
