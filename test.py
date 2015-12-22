def overlap(self, printen=True):
        missed = []
        true_positives = {}
        false_positives = []
        multiple_true_positives = {}
        for intervals_guacemole in self.guacemole.intervals_guacemole:
            positive = False
            positives = False
            for intervals_vcf in self.vcf.intervals_vcf:
                if self.positive_or_negative(intervals_vcf[0], intervals_vcf[1], intervals_guacemole[0],
                                             intervals_guacemole[1]):
                    if positive:
                        true_positives[str(intervals_guacemole)] += [intervals_vcf]
                        positives = True
                    else:
                        positive = True
                        true_positives.update({str(intervals_guacemole): [intervals_vcf]})
            if positive:
                if positives:
                    multiple_true_positives.update(
                        {str(intervals_guacemole): [true_positives[str(intervals_guacemole)]]})
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
            print("missed " + str(missed.__len__()))
            print("true_positives " + str(true_positives.__len__()))
            print("false_positives " + str(false_positives.__len__()))
            print("multiple_true_positives " + str(multiple_true_positives.__len__()))
            print("number of intervals guacemole " + str(self.guacemole.intervals_guacemole.__len__()))
            print("number of intervals vcf " + str(self.vcf.intervals_vcf.__len__()))
            print("missed " + str(missed))
            print("true_positives " + str(true_positives))
            print("false_positives " + str(false_positives))
            print("multiple_true_positives " + str(multiple_true_positives))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives