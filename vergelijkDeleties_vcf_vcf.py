#!/usr/bin/env python
#from vcf_vcf.vcf import Vcf
from vcf import Vcf

class Vergelijk():

    def __init__(self):
        pass

    def __laden__(self, delSelf, path_vcf, path_vcf_t, chr):
        self.vcft = Vcf(path_vcf_t, chr)
        self.vcft.deletion(delSelf)
        self.vcft.lees_vcf()
        self.vcf = Vcf(path_vcf, chr)
        self.vcf.deletion(delSelf)
        self.vcf.lees_vcf()

    def positive_or_negative(self, interval_vcft_start, interval_vcft_stop, interval_vcf_start, interval_vcf_stop):
        interval_vcft = interval_vcft_stop - interval_vcft_start
        interval_vcf = interval_vcf_stop - interval_vcf_start
        if interval_vcft >= interval_vcf:
            if (interval_vcft_start <= interval_vcf_start <= interval_vcft_stop) or (interval_vcft_start <= interval_vcf_stop <= interval_vcft_stop):
                return True
            else:
                return False
        else:
            if (interval_vcf_start < interval_vcft_start < interval_vcf_stop) or (interval_vcf_start < interval_vcft_stop < interval_vcf_stop):
                return True
            else:
                return False

    def overlap(self, printen= True):
        missed = []
        true_positives = {}
        false_positives = []
        multiple_true_positives = {}
        for intervals_vcf in self.vcf.intervals_vcf:
            positive = False
            positives = False
            for intervals_vcft in self.vcft.intervals_vcf:
                if self.positive_or_negative(intervals_vcft[0], intervals_vcft[1], intervals_vcf[0], intervals_vcf[1]):
                    if positive:
                        true_positives[str(intervals_vcf)] += [intervals_vcft]
                        positives = True
                    else:
                        positive = True
                        true_positives.update({str(intervals_vcf):[intervals_vcft]})
            if positive:
                if positives:
                    multiple_true_positives.update({str(intervals_vcf):[true_positives[str(intervals_vcf)]]})
            else:
                false_positives += [intervals_vcf]
        for intervals_vcft in self.vcft.intervals_vcf:
            mis = True
            for values in true_positives.values():
                for intervals in values:
                    if set(intervals) == set(intervals_vcft):
                        mis = False
            if mis:
                missed += [intervals_vcft]
        if printen:
            print("missed "+str(missed.__len__()))
            print("true_positives "+str(true_positives.__len__()))
            print("false_positives "+str(false_positives.__len__()))
            print("multiple_true_positives "+str(multiple_true_positives.__len__()))
            print("number of intervals vcf "+str(self.vcf.intervals_vcf.__len__()))
            print("number of intervals vcft "+str(self.vcf.intervals_vcft.__len__()))
            print("missed "+str(missed))
            print("true_positives "+str(true_positives))
            print("false_positives "+str(false_positives))
            print("multiple_true_positives "+str(multiple_true_positives))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives


def main():
    print("no main")

if __name__ == "__main__":
    main()