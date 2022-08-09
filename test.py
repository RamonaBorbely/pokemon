from utils import *
import csv

# startup()
# #
# # print(check_poke())
# # print(add_poke())
#
pokedex = load_pokes('pokemon_database.csv')
print(pokedex)

# by_name(pokedex)
# save_pokes(pokedex)



add_specific_poke()











# # functions with lower() not work
# def load_poks(path):
#     with open(path) as file:
#         data = csv.reader(file)
#         poks_list = [row for row in data]
#     return poks_list
#
#
# pokdex = load_poks('pokemon_database.csv')
# print(pokdex)
#
#
# def search_by_name(p_list):
#     chosen_pokemon = input("Enter pokemon's name: ")
#     for pokemon in p_list:
#         if chosen_pokemon in pokemon:
#             print(pokemon)
#
#
# search_by_name(pokdex)

# without functions. lower() still does not work
# with open('pokemon_database.csv') as file:
#     data = csv.reader(file)
#     poks_list = [row for row in data]
#
# print(poks_list)
#
# chosen_pokemon = input("Enter pokemon's name: ")
# for pokemon in poks_list:
#     if chosen_pokemon in pokemon:
#         print(pokemon)










