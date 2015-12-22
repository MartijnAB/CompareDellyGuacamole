 def positive_or_negative(self, interval_vcf_start, interval_vcf_stop, interval_guacemole_start,
                             interval_guacemole_stop):
        interval_vcf = interval_vcf_stop - interval_vcf_start
        interval_guacemole = interval_guacemole_stop - interval_guacemole_start
        if interval_vcf >= interval_guacemole:
            if (interval_vcf_start <= interval_guacemole_start <= interval_vcf_stop) or (
                    interval_vcf_start <= interval_guacemole_stop <= interval_vcf_stop):
                return True
            else:
                return False
        else:
            if (interval_guacemole_start < interval_vcf_start < interval_guacemole_stop) or (
                    interval_guacemole_start < interval_vcf_stop < interval_guacemole_stop):
                return True
            else:
                return False