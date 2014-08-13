class Classifier(object):

    def __init__(self, lovefile, hatefile):
        self.lovedata = self.read_file(lovefile)
        self.hatedata = self.read_file(hatefile)

    def read_file(self, filename):
        with open(filename) as f:
            array=f.read().splitlines()
            array=[" " + x.upper() for x in array]
        return array

    #todo 'rip' matches on 'tripping' bug (just starting from)
    #todo if previous word is 'not' or 'n't' then invert meaning;
    #todo if previous is 'really', 'very' then add one point (Intensifier page on wiki)

    # True if good, False if bad
    def classify(self, str):

        pr_str = self.prepare_str(str)
        love = 0
        for word in self.lovedata:
            # c = str.count(word)
            # if c!= 0 : print 'love: ' + word
            love += pr_str.count(word)

        hate = 0
        for word in self.hatedata:
            # c = str.count(word)
            # if c!= 0 : print 'hate: ' + word
            hate += pr_str.count(word)

        if (love + hate != 0) : return (float(love) - hate) / (love + hate)
        else: return 0;

    def prepare_str(self, str):
        return " " + str.upper()

if __name__ == "__main__":
    cl = Classifier('lists/lovelist.txt', 'lists/hatelist.txt')
    print cl.classify("The weather is awful")
    print cl.classify("Oh god! I love them!!!")
    print cl.classify("Bieber sucks!!!!1111")
    print cl.classify("The sleep to work ratio in life is just fucked upppp on some shit")
