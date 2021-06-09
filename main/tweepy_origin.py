import tweepy
import json

class Twitter:
    def __init__(self):
        # jsonファイルからキー取得
        FILENAME = "my_key.json"
        fd = open(FILENAME, mode='r')
        data = json.load(fd)
        fd.close()
        # 取得した各種キーを格納-----------------------------------------------------
        consumer_key = data["consumer_key"]
        consumer_secret = data["consumer_secret"]
        access_token = data["access_token"]
        access_token_secret = data["access_token_secret"]
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweet_nolinks(self,word):
        result = {"status":200,"word":word,"num":0,"urls":[],"text":[]}
        try:
            q_word = word + " -filter:retweets -filter:links"
            tweets = self.api.search(q=q_word, count=100, exclude_replies=True)
            result["num"] = len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1,exclude_replies=True)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1,exclude_replies=True)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1,exclude_replies=True)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1,exclude_replies=True)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
        except:
            if result["num"] < 1:
                result["status"] = 404
        return result

    def get_tweet(self,word):
        result = {"status":200,"word":word,"num":0,"urls":[],"text":[]}
        try:
            q_word = word + " -filter:retweets"
            tweets = self.api.search(q=q_word, count=100)
            result["num"] = len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
            tweets = self.api.search(q=q_word, count=100, max_id=tweets[-1].id-1)
            result["num"] += len(tweets)
            for tweet in tweets:
                result["urls"].append(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                result["text"].append(tweet.text)
        except:
            if result["num"] < 1:
                result["status"] = 404
        return result

def main():
    twitter = Twitter()
    result = twitter.get_tweet("テスト",10)
    print(result)

if __name__ == "__main__":
    main()