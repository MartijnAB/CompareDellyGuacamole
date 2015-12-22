 def positive_or_negative(self, interval_vcft_start, interval_vcft_stop, interval_vcf_start, interval_vcf_stop):
        interval_vcft = interval_vcft_stop - interval_vcft_start
        interval_vcf = interval_vcf_stop - interval_vcf_start
        if interval_vcft >= interval_vcf:
            if (interval_vcft_start <= interval_vcf_start <= interval_vcft_stop) or (
                    interval_vcft_start <= interval_vcf_stop <= interval_vcft_stop):
                return True
            else:
                return False
        else:
            if (interval_vcf_start < interval_vcft_start < interval_vcf_stop) or (
                    interval_vcf_start < interval_vcft_stop < interval_vcf_stop):
                return True
            else:
                return False