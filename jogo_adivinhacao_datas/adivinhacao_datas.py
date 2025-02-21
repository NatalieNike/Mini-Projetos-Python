import json
import random

f = open("jogo_adivinhacao_datas/words.json", encoding="utf8")

words = json.load(f)
print(words["25011654"])
random.choice(list(words.keys()))