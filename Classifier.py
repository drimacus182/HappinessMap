class Classifier(object):

    def __init__(self, lovefile, hatefile):
        self.lovefile = lovefile
        self.hatefile = hatefile

    def read_file(self, filename):
        with open(filename) as f:
            array=f.readlines()

        return array


    # True if good, False if bad
    def classify(self, string):




        return True