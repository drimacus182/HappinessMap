class Classifier(object):

    def __init__(self, lovefile, hatefile):
        self.lovedata = self.read_file(lovefile)
        self.hatedata = self.read_file(hatefile)

    def read_file(self, filename):
        with open(filename) as f:
            array=f.read().splitlines()
        return array

    # True if good, False if bad
    def classify(self, str):
        love = 0
        for word in self.lovedata:
            love += str.count(word)

        hate = 0
        for word in self.hatedata:
            c = str.count(word)
            hate += str.count(word)

        if (love + hate != 0) : return love - hate / (love + hate)
        else: return 0;


if __name__ == "__main__":
    cl = Classifier('lists/lovelist.txt', 'lists/hatelist.txt')
    print cl.classify("The weather is awful")
