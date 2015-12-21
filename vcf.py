import re, sys
class vcf():


    def __init__(self, file, chromosomes= False):
        self.file = file
        if chromosomes:
            fill = "("
            if re.match(",",chromosomes):
                for number in chromosomes.split(","):
                    fill += number + "|"
                fill = fill[:-1]
            else:
                fill += chromosomes
            self.chromosome =  fill+")" # chromosme numbers 1,2,4

    def deletion(self, size):
        file = open(self.file, "r")
        vcfContent = file.read()
        text = ""
        if vcfContent.startswith("##fileformat=VCFv4.0"):
            for x in re.findall("\n"+self.chromosome+"\t(\d+)\t.+\t([ATCG]+)\t([ATCG]+).+", vcfContent):
                if x[2].__len__() > x[3].__len__():
                    if (x[2].__len__() - x[3].__len__()) >size:
                        if "," not in x[-1]:
                            text += x[1]+"|"+str(int(x[1])+x[2].__len__())+"\n"
        if vcfContent.startswith("##fileformat=VCFv4.1"):
            for x in re.findall("\n"+self.chromosome+"\t(\d+)\t.+\<DEL\>.+END=(\d+).+", vcfContent):
                if (int(x[2])-int(x[1])) > size:
                    text+=x[1]+"|"+x[2]+"\n"
        self.v_c_f = text
        self.vcf_exists = True
        file.close()


    def make_file(self, paht="uikomst.simu.truth.vcf.chr20.posie.allen.deleetsie"):
        if self.vcf_exists:
            mijntekxt = open(paht, "w")
            mijntekxt.write(self.v_c_f)
            mijntekxt.close()
        else:
            print("no vcf")
            sys.exit(0)

    def lees_vcf(self):
        if self.vcf_exists:
            self.intervals_vcf = [ [int(number[0]), int(number[1])] for number in [numbers.split("|") for numbers in self.v_c_f.split("\n")][:-1]]
        else:
            print("no vcf")
            sys.exit(0)


def main():
    print("a")
    test = vcf("../vcfverelijk/simu.truth.vcf", "20,21")
    print(test.chromosome)
    test.deletion(300)
    print(test.v_c_f)
    print("aaaa")
    test.lees_vcf()
    print(test.intervals_vcf)
    print("a")






if __name__ == "__main__":
    main()