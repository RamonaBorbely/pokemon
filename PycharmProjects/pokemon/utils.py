import csv
import random


def startup():
    print("\t"*7,  "Pokemon App")


def options():
    print("MENU:\n1-Check your Pokemon\n2-Add a new Pokemon\n3-Show all Pokemon\n4-Visualise\n5-Save your "
          "Pokedex\n0-Exit")
    opt = int(input("Enter an option from menu: "))
    if opt in [1,2,3,4,5,0]:
        return opt
    else:
        return None


def check_poke():
    print("How to search the pokemon:\n1-By name\n2-By type")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def add_poke():
    print("How to add the pokemon:\n1-Add specific\n2-Add at random")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def visualise():
    print("How to produce the graph:\n1-By Generation (Pie Chart)\n2-By Type (Bar Chart)")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def by_name(p_list):
    # t6
    chosen_pokemon = input("Choose a pokemon by name: ").title()
    for pokemon in p_list:
        if chosen_pokemon in pokemon:
            print(f"At line: {pokemon[0]} Name: {pokemon[1]}, Type1: {pokemon[2]}, Type2: {pokemon[3]}, Total: {pokemon[4]}, HP: {pokemon[5]}, Generation: {pokemon[11]} ")


def by_type(p_list):
    # t7
    chosen_pokemon = input("Choose a pokemon by type: ").title()
    for pokemon in p_list:
        if chosen_pokemon in pokemon:
            print(f"At line: {pokemon[0]} Name: {pokemon[1]}, Type1: {pokemon[2]}, Type2: {pokemon[3]}, Total: {pokemon[4]}, HP: {pokemon[5]}, Generation: {pokemon[11]} ")


def add_specific_poke():
    # t8
    pokedex = load_pokes("pokemon_database.csv")
    pokemon_to_add = input("Enter pokemon's name: ").title()
    new_pokedex = [pokemon for pokemon in pokedex if pokemon[1] == pokemon_to_add]
    return new_pokedex


def add_random_poke():
    # t9
    pokedex = load_pokes("pokemon_database.csv")
    new_pokedex = random.choice(pokedex)
    return new_pokedex


def show_all(pokedex):
    # t10
    pokedex = load_pokes('pokemon_database.csv')
    for row in pokedex:
        print(f"Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, Total: {row[4]}, HP: {row[5]}, Generation: {row[11]} ")


def save_pokes(pokedex):
    # t11
    with open("new_pokemon_database.csv", "w") as file:
        to_write = csv.writer(file, delimiter='\n')
        to_write.writerow(pokedex)


def load_pokes(path):
    # t11.5
    with open(path) as pokemon_data:
        data = csv.reader(pokemon_data)
        pokemon_list = [row for row in data]
    return pokemon_list


