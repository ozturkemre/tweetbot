def rt(api,tweepy,sleep):
    for tweet in tweepy.Cursor(api.search, q='#galatasaray', since='2017-08-12', until='2017-08-13', lang='tr').items():
        try:
            print('Tweet by: @' + tweet.user.screen_name)
            tweet.retweet()
            print('Retweeted the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        sleep(60)