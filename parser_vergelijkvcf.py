from vergelijkDeleties_vcf_vcf import vergelijk
import argparse


class parser():

    def __init__(self):
        pars = argparse.ArgumentParser(description='compare del truth vcf with  del vcf.')
        pars.add_argument('--path', help='path vcf')
        pars.add_argument('--print', help='print info')
        pars.add_argument('--write', help='niet none= normol 2= all')
        pars.add_argument('--writename', help='name')
        delSelf = input("del")
        args = pars.parse_args()
        runSelf = vergelijk()
        runSelf.__laden__(int(delSelf), args.path)
        runSelf.overlap(args.print)
        if args.writename:
            writ = open("files/"+args.writename, "w")
            if args.write:
                writ.write("missed "+ str(runSelf.missed.__len__())+"\n")
                writ.write("true_positives "+ str(runSelf.true_positives.__len__())+"\n")
                writ.write("false_positives "+ str(runSelf.false_positives.__len__())+"\n")
                writ.write("multiple_true_positives "+str(runSelf.multiple_true_positives.__len__())+"\n")
                writ.write("number of intervals in delly vcf "+ str(runSelf.vcf.intervals_vcf.__len__())+"\n")
                writ.write("number of intervals in thrie vcf "+ str(runSelf.vcft.intervals_vcf.__len__())+"\n")
            if args.write == "2":
                 writ.write("missed "+ str(runSelf.missed)+"\n")
                 writ.write("true_positives "+ str(runSelf.true_positives)+"\n")
                 writ.write("false_positives "+ str(runSelf.false_positives)+"\n")
                 writ.write("multiple_true_positives "+str(runSelf.multiple_true_positives)+"\n")
            writ.close()

def main():
    run = parser()

if __name__ == "__main__":
    main()