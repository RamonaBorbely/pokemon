import matplotlib.pyplot as plt


def pie_chart(pokedex):
    # t27
    pokemon_generations = [pokemon[11] for pokemon in pokedex[1:]]
    plt.pie(list(set(pokemon_generations)), labels=list(set(pokemon_generations)), autopct="%.0f")
    plt.title("Pokemons by generation")
    plt.show()


def bar_chart(pokedex):
    # t28
    pokemon_types = [pokemon[2] for pokemon in pokedex[1:]]
    plt.bar(pokemon_types, len(pokemon_types))
    plt.title("Pokemons by type")
    plt.show()

