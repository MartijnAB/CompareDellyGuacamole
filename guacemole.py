import re
class guacemole():

    def __init__(self, path):
        self.path = path


    def __load__(self):
        uikomstguacemoel = open(self.path , "r")
        self.guacemole = uikomstguacemoel.read()
        uikomstguacemoel.close()

    def lees_guacemole(self, size):
        self.intervals_guacemole = []
        for  GenomeRange in [[int( numbers.split(",")[0]), int( numbers.split(",")[1])] for  numbers in re.findall("21,(\d+,\d+)", self.guacemole.split("List")[1])]:
            if  GenomeRange[0] < GenomeRange[1]:
                if (int(GenomeRange[1]) - int(GenomeRange[0])) > size:
                    self.intervals_guacemole += [GenomeRange]
            else:
                if (int(GenomeRange[0]) - int(GenomeRange[1])) > size:
                    self.intervals_guacemole += [[GenomeRange[1], GenomeRange[0]]]



def main():
    print("a")
    test = guacemole("/Users/martijn/spark-1.5.2-bin-hadoop2.6/bin/eerstcukmoluitkomst/part-00000")
    test.__load__()
    test.lees_guacemole()
    print(test.getaallen_guacemole)
    print("a")






if __name__ == "__main__":
    main()