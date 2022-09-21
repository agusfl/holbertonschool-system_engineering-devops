#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re setting
a custom User-Agent.

Requirements:

- Prototype: def number_of_subscribers(subreddit)
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.

How to set User-Agent:
https://stackoverflow.com/questions/10606133/%20sending-user-agent-using-
requests-library-in-python

Info request module python: https://realpython.com/python-requests/
"""
import requests


def number_of_subscribers(subreddit):
    """
    Count number of subreddits
    """

    # Esta va a ser la URL a la que vamos a hacer una request, subreddit va a
    # ser el "tema" que se pase como argumento en linea para retornar la
    # cantidad de subscriptores de dicho tema.
    url_subredit = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = requests.utils.default_headers()

    # Seteamos el User-Agent para no tener problemas de "too many requests"
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )

    # Hacemos una request de la url indicada arriba con el metodo GET
    res = requests.get(url_subredit, headers=headers)

    # Pasar datos a JSON para obtener un diccionario de python y poder
    # trabajar con los datos en python
    json_res = res.json()

    # Chequeamos si la respuesta fue existosa (status code = 200) significa que
    # el subredit existe. Si la respuesta no fue existosa (no dio status code
    # 200) es porque no existe ese "tema", por lo tanto retornamos 0
    if res.status_code == 200:
        # Traemos el atributo data del diccionario "res" que nos devolvio el
        # .json y dentro del atributo data buscamos la cantidad de subscribers
        # Usamos la nomenclatura para acceder a diccionarios de python
        return json_res['data']['subscribers']
    else:
        return 0
