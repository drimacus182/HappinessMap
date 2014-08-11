from TwitterAPI import TwitterAPI

def registerApi():
    api = TwitterAPI("BGMUpePgUoFU13l3NOd26DVUD",
                     "pmiwqlftwhj6tPEDBzRrxvObSw3E8Kt29PIUo0XjGW60jtpOZO",
                     "2719912512-l6a59JAHMpbs8s5t72BHLJqL19sCvUluBw9Ewhh",
                     "1QNsRQKJ6eRTxY9x8HQ3RcdwNd48IF4ywk0MWFI0ILqG7")
    return api

def registerTweetCallback(callback):
    api = registerApi()

    #Stream tweets from New York City:
    r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
    for item in r.get_iterator():
        callback(item)

#TODO Insert handling code here
def callback(item):
    print item
    return

if __name__ == "__main__":
    registerTweetCallback(callback)

##### Trash here


    #Get some tweets:
    # r = api.request('search/tweets', {'q':'pizza'})
    # for item in r.get_iterator():
    #     print item
