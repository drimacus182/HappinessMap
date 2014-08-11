def callb(item):
    print item
    return

class TwitterGetter(object):

    def __init__(self):
        self.stop = False
        self.registerApi()

    @property
    def headers(self):
        return self.api

    def registerApi(self):
        from TwitterAPI import TwitterAPI
        self.api = TwitterAPI("BGMUpePgUoFU13l3NOd26DVUD",
                         "pmiwqlftwhj6tPEDBzRrxvObSw3E8Kt29PIUo0XjGW60jtpOZO",
                         "2719912512-l6a59JAHMpbs8s5t72BHLJqL19sCvUluBw9Ewhh",
                         "1QNsRQKJ6eRTxY9x8HQ3RcdwNd48IF4ywk0MWFI0ILqG7")

    def registerCallback(self, callback):
        self.callback = callback

    def startFlow(self):
        r = self.api.request('statuses/filter', {'locations':'-179.1506, 18.9117, -66.9406, 71.4410'})
        for item in r.get_iterator():
            # if item['coordinates'] != None:
            #     print item['coordinates']['coordinates']
            self.callback(item)

            if self.stop : break

    def stopFlow(self):
        self.stop = True

# Basic usage here:::

if __name__ == "__main__":
    tgetter = TwitterGetter()
    tgetter.registerApi()
    tgetter.registerCallback(callb)
    tgetter.startFlow()
    # then tgetter.stopFlow()
