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
        if options() == 1:
            if check_poke() == 1:
                by_name(pokedex)
            else:
                by_type(pokedex)
        elif options() == 2:
            if add_poke() == 1:
                add_specific_poke()
            else:
                add_random_poke()
        elif options() == 3:
            show_all(pokedex)
        elif options() == 4:
            if visualise() == 1:
                pie_chart(pokedex)
            else:
                bar_chart(pokedex)
        elif options() == 5:
            save_pokes(pokedex)
        elif options() == 0:
            break

    # # t 17- 26



run()


