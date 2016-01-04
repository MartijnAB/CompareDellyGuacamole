class Compare():
    def __load__(self, alt, ref):
        self.alt = alt
        self.ref = ref

    def positive_or_negative(self, interval_alt_start, interval_alt_stop, interval_ref_start, interval_ref_stop):
        interval_alt = interval_alt_stop - interval_alt_start
        interval_ref = interval_ref_stop - interval_ref_start
        if interval_alt >= interval_ref:
            if (interval_alt_start <= interval_ref_start <= interval_alt_stop) or (
                    interval_alt_start <= interval_ref_stop <= interval_alt_stop):
                return True
            else:
                return False
        else:
            if (interval_ref_start < interval_alt_start < interval_ref_stop) or (
                    interval_ref_start < interval_alt_stop < interval_ref_stop):
                return True
            else:
                return False

    def overlap(self, printing=True):
        missed = []
        true_positives = {}
        false_positives = []
        multiple_true_positives = {}
        for intervals_alt in self.alt.intervals:
            positive = False
            positives = False
            for intervals_ref in self.ref.intervals:
                if self.positive_or_negative(intervals_alt[0], intervals_alt[1], intervals_ref[0],
                                             intervals_ref[1]):
                    if positive:
                        true_positives[str(intervals_alt)] += [intervals_ref]
                        positives = True
                    else:
                        positive = True
                        true_positives.update({str(intervals_alt): [intervals_ref]})
            if positive:
                if positives:
                    multiple_true_positives.update(
                        {str(intervals_alt): [true_positives[str(intervals_alt)]]})
            else:
                false_positives += [intervals_alt]
        for intervals_ref in self.ref.intervals:
            mis = True
            for values in true_positives.values():
                for intervals in values:
                    if set(intervals) == set(intervals_ref):
                        mis = False
            if mis:
                missed += [intervals_ref]
        if printing:
            print("missed " + str(missed.__len__()))
            print("true_positives " + str(true_positives.__len__()))
            print("false_positives " + str(false_positives.__len__()))
            print("multiple_true_positives " + str(multiple_true_positives.__len__()))
            print("number of intervals alt " + str(self.alt.intervals.__len__()))
            print("number of intervals ref " + str(self.ref.intervals.__len__()))
            print("missed " + str(missed))
            print("true_positives " + str(true_positives))
            print("false_positives " + str(false_positives))
            print("multiple_true_positives " + str(multiple_true_positives))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives