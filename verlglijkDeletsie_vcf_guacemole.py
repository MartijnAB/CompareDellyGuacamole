#!/usr/bin/env python
#from vcf_guacemole.vcf import vcf
#from vcf_guacemole.guacemole import guacemole
from vcf import vcf
from guacemole import guacemole


class vergelijk():

    def __init__(self):
        pass

    def __laden__(self, delSelf= 300, path_Guacemole="/Users/martijn/spark-1.5.2-bin-hadoop2.6/bin/eerstcukmoluitkomst/part-00000", path_vcf="../vcfverelijk/simu.truth.vcf", chr="21"):
        print(path_Guacemole)

        self.vcf = vcf(path_vcf, chr)
        self.vcf.deletion(delSelf)
        self.vcf.lees_vcf()
        self.guacemole = guacemole(path_Guacemole)
        self.guacemole.__load__()
        self.guacemole.lees_guacemole(delSelf)

    def positive_or_negative(self, interval_vcf_start, interval_vcf_stop, interval_guacemole_start, interval_guacemole_stop):
        interval_vcf = interval_vcf_stop - interval_vcf_start
        interval_guacemole = interval_guacemole_stop - interval_guacemole_start
        if interval_vcf >= interval_guacemole:
            if (interval_vcf_start <= interval_guacemole_start <= interval_vcf_stop) or (interval_vcf_start <= interval_guacemole_stop <=  interval_vcf_stop):
                return True
            else:
                return False
        else:
            if (interval_guacemole_start < interval_vcf_start < interval_guacemole_stop) or (interval_guacemole_start < interval_vcf_stop <  interval_guacemole_stop):
                return True
            else:
                return False

    def overlap(self, printen= True):
        missed = []
        true_positives = {}
        false_positives = []
        multiple_true_positives = {}
        for intervals_guacemole in self.guacemole.intervals_guacemole:
            positive = False
            positives = False
            for intervals_vcf in self.vcf.intervals_vcf:
                if self.positive_or_negative(intervals_vcf[0], intervals_vcf[1], intervals_guacemole[0], intervals_guacemole[1]):
                    if positive:
                        true_positives[str(intervals_guacemole)] += [intervals_vcf]
                        positives = True
                    else:
                        positive = True
                        true_positives.update({str(intervals_guacemole):[intervals_vcf]})
            if positive:
                if positives:
                    multiple_true_positives.update({str(intervals_guacemole):[true_positives[str(intervals_guacemole)]]})
            else:
                false_positives += [intervals_guacemole]
        for intervals_vcf in self.vcf.intervals_vcf:
            mis = True
            for values in true_positives.values():
                for intervals in values:
                    if set(intervals) == set(intervals_vcf):
                        mis = False
            if mis:
                missed += [intervals_vcf]
        if printen:
            print("missed "+ str(missed.__len__()))
            print("true_positives "+ str(true_positives.__len__()))
            print("false_positives "+ str(false_positives.__len__()))
            print("multiple_true_positives "+str(multiple_true_positives.__len__()))
            print("number of intervals guacemole "+ str(self.guacemole.intervals_guacemole.__len__()))
            print("number of intervals vcf "+ str(self.vcf.intervals_vcf.__len__()))
            print("missed "+ str(missed))
            print("true_positives "+ str(true_positives))
            print("false_positives "+ str(false_positives))
            print("multiple_true_positives "+str(multiple_true_positives))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives


def main():
    reken = vergelijk()
    reken.__laden__()
    reken.overlap()

if __name__ == "__main__":
    main()