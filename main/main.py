from tweepy_origin import Twitter
from janome_origin import morphological_analysis
from markov_chain import Markov_2, Markov
from time import time

class Shittakater:
    def __init__(self):
        self.twitter = Twitter()
        self.result = {"status":0,"word":""}
        self.is_ok = False
        self.mar = Markov()
        self.mar2 = Markov_2()

    def lean(self,word):
        self.result = self.twitter.get_tweet(word)
        if self.result["status"] != 200 or self.result["num"] < 100:
            self.is_ok = False
        else:
            texts = morphological_analysis(self.result["text"])
            self.mar.reset()
            self.mar.lean(texts)
            self.mar2.reset()
            self.mar2.lean(texts)
            self.is_ok = True

    def make(self):
        if self.is_ok:
            self.result["result"] = self.mar.make()
            self.result["result2"] = self.mar2.make()

def main():
    # s = input(f"欲しい単語を入力してね：")
    s = "剣持"
    shittakater = Shittakater()
    shittakater.lean(s)
    print(shittakater.mar.model)
    print(shittakater.mar2.model)
    if shittakater.is_ok:
        shittakater.make()
        print(shittakater.result["result"]+"\n_______")
        print(shittakater.result["result2"]+"\n_______")
        shittakater.make()
        print(shittakater.result["result"]+"\n_______")
        print(shittakater.result["result2"]+"\n_______")

if __name__ == "__main__":
    main()