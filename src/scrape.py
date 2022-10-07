"""This module scrapes the web, transforms and sanitizes web data."""
from loguru import logger
import lxml
import lxml.html as lh
import pandas as pd
from pydantic import AnyUrl, ValidationError
import requests
from typing import List, Dict


NUM_POKE_STATS = 10
TABLE_COL_NAMES_STR = ["#", "Name", "Type"]


def get_webpage_html(url_path: AnyUrl) -> bytes:
    """Tries to request the given webpage.

    Args:
        url_path: string of url path to webpage

    Returns:
        page_contents: the response of the request to get the webpage
    """
    page_contents = None

    try:
        logger.info(f"Attempting to access given URL: {url_path}...")
        page = requests.get(url_path)
        page_contents = page.content
        status = page.status_code

        if status == 200:
            logger.success("Returning webpage contents...")

    except (ValidationError, requests.exceptions.MissingSchema) as e:
        logger.exception(e)
        logger.error("Error: check URL is correct schema and name.")

    return page_contents


def get_webpage_html_elements(page_contents: bytes) -> List[lxml.html.HtmlElement]:
    """Parses the page contents of a webpage and extracts the HTML elements.

    Args:
        page_contents: the response of the request to get the webpage

    Returns:
        text_between_tr_html: parsed webpage data stored between <tr>..</tr> of HTML
    """
    doc = lh.fromstring(page_contents)
    text_between_tr_html = doc.xpath("//tr")
    return text_between_tr_html


def get_pokemon_from_html_table(
    text_between_tr_html: List[lxml.html.HtmlElement],
) -> Dict:
    """Parses the page contents of a webpage and extracts the HTML elements.

    Args:
        text_between_tr_html: parsed webpage data stored between <tr>..</tr> of HTML

    Returns:
        pokedex: pokemon stat names and attributes as string values
    """
    # make pokedex data columns
    pokedex_data = [(element.text_content(), []) for element in text_between_tr_html[0]]
    titles = [element.text_content() for element in text_between_tr_html[0]]
    # constructing the pokedex this way avoids a transpose in the pandas dataframe later
    # pokedex_data = [[]] * len(titles) transposes rows and columns for some reason
    pokedex_data = [[] for i in range(len(titles))]

    # fill in pokedex data from body of table so skip header at index 0
    for table_row in text_between_tr_html[1:]:

        # If row is not of size 10 then the //tr data is not from our table
        if len(table_row) != NUM_POKE_STATS:
            break

        pokemon_attributes = list(table_row.iterchildren())
        for i in range(NUM_POKE_STATS):
            poke_stat = pokemon_attributes[i].text_content()
            pokedex_data[i].append(poke_stat)

    pokedex = {title: pokedex_data[i] for i, title in enumerate(titles)}
    return pokedex


def make_pokedex_dataframe(pokedex: Dict) -> pd.DataFrame:
    """Makes a pandas dataframe from the pokemon table values.

    Args:
        pokedex: pokemon stat names and attributes as string values

    Returns:
        df: pokemon stat names and attributes as a pandas dataframe
    """
    df = pd.DataFrame(pokedex)

    # convert numeric stats to integers
    for name in df.columns:
        if name not in TABLE_COL_NAMES_STR:
            df[name] = pd.to_numeric(df[name], downcast="integer")

    logger.success("Returning pokedex as Pandas DataFrame...")

    return df
