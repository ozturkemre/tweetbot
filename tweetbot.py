import tweepy
from getOAuth import *
from liveScores import *
from time import sleep
# from fromFile import *
# from retw import *
# from favorite import *
# from fol import *
# from unfol import *


def do_the_job():
    doc = connect()
    scores = get_scores(doc)
    return scores


def score_print(publish):

    ready_tweet = publish["minute"] + "' " + publish["home"] + " " + publish["score"] + " " + publish["away"] + " " + "#livescore"

    try:
        tweet_from_app(api, ready_tweet)

    except:
        pass


def tweet_from_app(api, tw):
    api.update_status(status=str(tw))

# getting Auth
api = getAuth(tweepy)

old_scores = do_the_job()
print(old_scores)
sleep(5)

while True:
    try:
        new_scores = do_the_job()
        finished = []
        for i in old_scores:
            if i in new_scores:
                # if match live
                if old_scores[i]["score"] != new_scores[i]["score"] or (new_scores[i]["minute"] == "HT" and old_scores[i]["minute"] != "HT"):
                    if "color:red" in new_scores[i]["score"]:
                        pass
                    else:
                        # if scores or half time
                        score_print(new_scores[i])
                        pass

                old_scores[i] = new_scores[i]

            else:

                # if match finished
                old_scores[i]["minute"] = "FT"
                score_print(old_scores[i])
                finished.append(i)

        for i in new_scores:
            if i in old_scores:
                pass
            else:
                # if new match starts
                old_scores[i] = new_scores[i]
                # score_print(old_scores[i])

        for i in finished:
            # delete finished match
            del old_scores[i]

        sleep(20)
    except Exception as e:
        f=open("log.txt", "w")
        f.write("An exceptional thing happened ",e)
        f.close()



# tweet_from_app()
# tweet_from_file(api, tweepy, sl)

# rt(api, tweepy,sl)

# fav(api, tweepy, sl)


# foll(api, tweepy, sl)

# unfoll(api, tweepy, sl)
