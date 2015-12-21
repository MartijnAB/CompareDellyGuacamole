import argparse

import sys


class Pars:
    def __init__(self):
        print("start programa")
        self.rtyp = "vcf"
        self.atyp = "vcf"

    def load_arguments(self):
        parser = argparse.ArgumentParser(description='alt vs ref')
        parser.add_argument('-alt', type=str, help='als vcf or out guacemole')
        parser.add_argument('-ref', type=str, help='ref vcf or out guacemole')
        parser.add_argument('-atyp', type=str, help='Typ alt. Is it vcf or guacemele?\tdefault = vcf')
        parser.add_argument('-rtyp', type=str, help='Typ ref. Is it vcf or guacemele?\tdefault = vcf')
        args = parser.parse_args()
        if args.alt == None or args.ref == None:
            print("you must specify an -alt and -ref otherwise the program stops")
            print("use -h for help")
            sys.exit()
        self.alt = args.alt
        self.ref = args.ref
        if args.rtyp.lower() == "vcf" or "guacemole":
            self.rtyp = args.rtyp
        if args.atyp.lower() == "vcf" or "guacemole":
            self.atyp = args.rtyp


def main():
    run = Pars()
    run.load_arguments()



if __name__ == '__main__':
    main()
