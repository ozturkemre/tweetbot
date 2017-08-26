import requests
from credentials import *


def connect():

    headers = {'User-Agent': 'Mozilla/5.0'}

    # get content of page
    content = requests.get(page, headers=headers).json()

    return content


def get_scores(doc):
    scores = {}
    for i in doc['data']:
        home_team = i['T1']
        away_team = i['T2']
        minute = i['MI']
        score = i['R']
        
        if "red card" in home_team:
            home_team = home_team.split("/>")[-1]

        if "red card" in away_team:
            away_team = away_team.split("<img")[0]

        if "<b>" in home_team:
            home_team = home_team.replace("<b>", "")
            home_team = home_team.replace("</b>", "")
            
        if "<b>" in away_team:
            away_team = away_team.replace("<b>", "")
            away_team = away_team.replace("</b>", "")

        if "color:red" in score:
            score = score.replace('<b style="color:red">', '')
            score = score.replace('</b>', '')

        scores[home_team] = {"minute": minute, "home": home_team, "away": away_team, "score": score}

    return scores
