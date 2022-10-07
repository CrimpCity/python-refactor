"""This module scrapes the web to make a pokemon pokedex."""
from src.scrape import (
    get_webpage_html,
    get_webpage_html_elements,
    get_pokemon_from_html_table,
    make_pokedex_dataframe,
)


if __name__ == "__main__":
    url = "http://pokemondb.net/pokedex/all"

    # CAN TURN ALL OF THIS CODE INTO ONE LINE OF CODE WITH pd.read_html
    page_contents = get_webpage_html(url)
    text_between_tr_html = get_webpage_html_elements(page_contents)
    pokedex_data = get_pokemon_from_html_table(text_between_tr_html)
    pokedex = make_pokedex_dataframe(pokedex_data)
    print(pokedex.head())
    print("\n")
    print(pokedex.dtypes)
