import json

f = open("gestao_aquario/gestao_aquario.json", encoding="utf8")

data_aquarium = json.load(f)
animals = data_aquarium["data"]

#filter

def verify_fish(animal):
    if animal["type"] == "fish":
        return True
    else:
        return False
    
#retorna os animais do tipo fish
animals_fish = list(filter(verify_fish, animals))
print(animals_fish)

#lambda

# Função lambda, é uma forma mais enxuta de escrever a função, sem declará-la, ela não é definida, não pode ser reusada então deve ser usada pontualmente, como no exemplo abaixo:
# animals_fish = list(filter(lambda animal: (animal["type"] == "fish"), animals))

#map

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name, animals_fish))
print(animals_fish_name)

#retorna os nomes dos animais do tipo fish

def assign_to_tank(animals, names_selected, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_selected:
            animal["tank number"] = new_tank_number
        return animal
    return list(map(change_tank_number, animals))

new_aquarium = assign_to_tank(animals, animals_fish_name, 42)
print(new_aquarium)

#continue