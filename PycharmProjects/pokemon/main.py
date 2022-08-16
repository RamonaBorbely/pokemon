from utils import *
from graphs import *

pokedex = []


def run():
    startup()
    global pokedex
    pokedex = load_pokes('pokemon_database.csv')
    #   RE-DO THIS
    while True:
    # t16
        opt = options()
        if opt == 1:
            if check_poke() == 1:
                by_name(pokedex)
            else:
                by_type(pokedex)
        elif opt == 2:
            if add_poke() == 1:
                add_specific_poke()
            else:
                add_random_poke()
        elif opt == 3:
            show_all(pokedex)
        elif opt == 4:
            if visualise() == 1:
                pie_chart(pokedex)
            else:
                bar_chart(pokedex)
        elif opt == 5:
            save_pokes(pokedex)
        elif opt == 0:
            break

    # # t 17- 26



run()


