#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.

Requirements:

- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.

How to set User-Agent:
https://stackoverflow.com/questions/10606133/%20sending-user-agent-using-
requests-library-in-python

Info request module python: https://realpython.com/python-requests/
"""
import requests


def top_ten(subreddit):
    """
    Return the first 10 hot posts listed in the subreddit passed as argument
    """
    # Chequeamos si la respuesta fue existosa (status code = 200) significa que
    # el subredit existe. Si la respuesta no fue existosa (no dio status code
    # 200) es porque no existe ese "tema", por lo tanto retornamos None
    try:
        # Esta va a ser la URL a la que vamos a hacer una request, subreddit va
        # a ser el "tema" que se pase como argumento en linea, usamos
        # "query string" para pasarle un limit a la request de 10 resultados
        url_sub = "https://www.reddit.com/r/{}/hot.json?limit=10"
        .format(subreddit)

        headers = requests.utils.default_headers()

        # Seteamos el User-Agent para no tener problemas de "too many requests"
        headers.update(
            {
                'User-Agent': 'My User Agent 1.0',
            }
        )

        # Hacemos una request de la url indicada arriba con el metodo GET
        res = requests.get(url_sub, headers=headers)

        # Pasar datos a JSON para obtener un diccionario de python y poder
        # trabajar con los datos en python
        json_res = res.json()

        # Traemos los top 10 de children
        top_ten = json_res['data']['children']

        # Se hace un for para imprimir cada uno de los 10 titulos que estan
        # en el top ten
        for title in top_ten:
            print(title['data']['title'])

    except Exception:
        print(None)
