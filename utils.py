'''Task 0: Import the modules csv and random'''
import csv
import random


def startup():    
    """Displays an entry message."""

    print("\t"*7,  "Pokemon App")


def options():
    """Displays main menu of options and read the user's response."""

    print("MENU:\n1-Check your Pokemon\n2-Add a new Pokemon\n3-Show all Pokemon\n4-Visualise\n5-Save your "
          "Pokedex\n0-Exit")
    opt = int(input("Enter an option from menu: "))
    if opt in [1,2,3,4,5,0]:
        return opt
    else:
        return None


def check_poke():
    """Displays a menu of options for how a Pokemon should be searched. Read in the user's response.
       return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("How to search the pokemon:\n1-By name\n2-By type")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def add_poke():
    """Reads in the user's response and adds a pokemon at a random or specific location"""

    print("How to add the pokemon:\n1-Add specific\n2-Add at random")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def visualise():
    """Displays a menu of options for how a graph should be produced. Read in the user's response.
        return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """

    print("How to produce the graph:\n1-By Generation (Pie Chart)\n2-By Type (Bar Chart)")
    opt = int(input("Enter an option from menu: "))
    if opt in [1, 2]:
        return opt
    else:
        return None


def by_name(p_list):
    
    """
    Task 6: Display a pokemon from the list, searching by name.

    The p_list is a list of pokemon.
    Prompt the user to enter name of the pokemon they are searching for.
    The function should display all the details related only to that single pokemon, if it's on the p_list.
    If pokemon of such name does not exist on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    chosen_pokemon = input("Choose a pokemon by name: ").title()
    for pokemon in p_list:
        if chosen_pokemon in pokemon:
            print(pokemon)



def by_type(p_list):
    
    """
    Task 7: Display pokemon from the list, searching by type.

    The p_list is a list of pokemon.
    Prompt the user to enter type of the pokemon they are searching for.
    The function should display all the details related only to pokemon of that type,
    if it's on the p_list.
    If no such pokemon of that type exists on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    chosen_pokemon = input("Choose a pokemon by type: ").title()
    for pokemon in p_list:
        if chosen_pokemon in pokemon:
            print(pokemon)


def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """
    # pokemon_list = load_pokes('pokemon_database.csv')
    # new_pokemon = input("Enter name of new pokemon: ")
    # for pokemon in pokemon_list:
    #     if new_pokemon not in pokemon:
    # return pokemon_list




def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """


def show_all(pokedex):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, total, hp and generation.

    :param p_list: None
    :return: None
    """
    pokedex = load_pokes('pokemon_database.csv')
    for row in pokedex:
        print(f"Name: {row[1]}, Type1: {row[2]}, Type2: {row[3]}, Total: {row[4]}, HP: {row[5]}, Generation: {row[11]} ")

def save_pokes(pokedex):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
    """
    with open("new_pokemon_databes.csv", "w") as file:
        to_write =  csv.writer(file, delimiter='\n')
        to_write.writerow(pokedex)

def load_pokes(path):
    """
    Task 11.5: Load up pokemon from a CSV file into a list structure
    :param path: A relative file path to CSV file in string format
    :return: A list of pokemon
    """

    with open(path) as pokemon_data:
        data = csv.reader(pokemon_data)
        pokemon_list = [row for row in data]

    return pokemon_list


