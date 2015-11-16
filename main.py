import requests
import json
import random
import sys


# text for different action
talk_text = "{} doit faire un talk de 10 minutes la semaine prochaine"
menage_text = "Aujourd'hui est un grand jour, c'est la lotterie du ménage ! \n\nLes grands gagnants sont :\n{}"

# our members for the lottery
with open("members.txt") as f:
    atilliens = f.read()[:-1].split("\n")

# t for talk or m for menage
action = sys.argv[1]
# incoming hook
hook = sys.argv[2]


def get_winner(nb):
    random.shuffle(atilliens)
    winner = atilliens[-nb::]
    return winner


if action == "t":
    t = talk_text
    w = get_winner(1)
elif action == "m":
    t = menage_text
    w = get_winner(4)
else:
    exit()


data = {
    "text": "<!everyone>\n" + t.format("\n".join(["- " + v for v in w]))
}

r = requests.post(hook, data = json.dumps(data))
