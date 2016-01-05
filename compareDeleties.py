class Compare:
    """
    This class provide everything needed to compare intervals as lists of intervals
    [[start, stop], [start, stop]].
    """

    def __init__(self, alt, ref):
        """The definition of the reference and the alternative.
        :param alt: The intervals represent the deletions as a list of lists containing the start end stop of the alternative.
        :param ref: The intervals represent the deletions as a list of lists containing the start end stop of the reference.
        """
        self.alt = alt
        self.ref = ref

    def positive_or_negative(self, interval_alt_start, interval_alt_stop, interval_ref_start, interval_ref_stop):
        """the position relative to each other is calculated of first base pair in the same direction.
        So that the length can be compared, to proof overlap.
        :param interval_alt_start: A int of the index of the start of a deletion in the alternative
        :param interval_alt_stop: A int of the index of the end of a deletion in the alternative
        :param interval_ref_start: A int of the index of the start of a deletion in the reference
        :param interval_ref_stop: A int of the index of the end of a deletion in the reference
        :return: A boolean true for overlap end false for no overlap.
        """

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

    def overlap(self):
        """overlap iterate over all the deletions en store the results in some variable en print some."""

        missed = []
        true_positives = {}
        false_positives = []
        multiple_true_positives = {}
        for intervals_alt in self.alt.intervals:  # Select all alternative deletions
            positive = False
            positives = False
            for intervals_ref in self.ref.intervals:  # Select all reference deletions
                if self.positive_or_negative(intervals_alt[0], intervals_alt[1], intervals_ref[0],
                                             intervals_ref[1]):  # Compare deletions (intervals)
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
        print("missed " + str(missed.__len__()))
        print("true positives " + str(true_positives.__len__()))
        print("false positives " + str(false_positives.__len__()))
        print("multiple true positives " + str(multiple_true_positives.__len__()))
        print("number of intervals alt " + str(self.alt.intervals.__len__()))
        print("number of intervals ref " + str(self.ref.intervals.__len__()))
        self.missed = missed
        self.true_positives = true_positives
        self.false_positives = false_positives
        self.multiple_true_positives = multiple_true_positives
