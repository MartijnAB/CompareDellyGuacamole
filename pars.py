import argparse


class Pars:
    def __init__(self):
        print("start programa")

    def load_arguments(self):
        parser = argparse.ArgumentParser(description='alt vs ref')
        parser.add_argument('-alt', type=str, help='als vcf or out guacemole')
        parser.add_argument('-ref', type=str, help='ref vcf or out guacemole')
        args = parser.parse_args()
        if args.alt == None or args.ref == None:
            print("ja")
        else:
            print("nee")


def main():
    run = Pars()
    run.load_arguments()


if __name__ == '__main__':
    main()
