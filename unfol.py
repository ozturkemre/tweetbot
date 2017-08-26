def unfoll(api, tweepy, sleep):
    for tweet in tweepy.Cursor(api.search, q='#galatasaray', since='2017-08-12', until='2017-08-13', lang='tr').items():
        try:
            print('Tweet by: @' + tweet.user.screen_name)
            if tweet.user.following:
                # Don't forget to indent
                tweet.user.unfollow()
                print('Unfollowed the user')
            else:
                print("User already unfollowed")

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        sleep(60)