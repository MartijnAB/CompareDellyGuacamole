 def overlap(self, printen=True):
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
                        true_positives.update({str(intervals_vcf): [intervals_vcft]})
            if positive:
                if positives:
                    multiple_true_positives.update({str(intervals_vcf): [true_positives[str(intervals_vcf)]]})
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
            print("missed " + str(missed.__len__()))
            print("true_positives " + str(true_positives.__len__()))
            print("false_positives " + str(false_positives.__len__()))
            print("multiple_true_positives " + str(multiple_true_positives.__len__()))
            print("number of intervals vcf " + str(self.vcf.intervals_vcf.__len__()))
            print("number of intervals vcft " + str(self.vcft.intervals_vcf.__len__()))
            print("missed " + str(missed))
            print("true_positives " + str(true_positives))
            print("false_positives " + str(false_positives))
            print("multiple_true_positives " + str(multiple_true_positives))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives