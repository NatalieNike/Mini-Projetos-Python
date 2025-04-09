import json

f = open("gestao_aquario/gestao_aquario.json", encoding="utf8")

data_aquarium = json.load(f)
animals = data_aquarium["data"]

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    else:
        return False
    
    #testetesteteste