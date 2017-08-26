my_file = open('verne.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

def tweet_from_file(api,tweepy,sleep):

    for line in file_lines:

        try:
            print(line)
            if line != '\n':
                api.update_status(status=line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)

        sleep(60)
