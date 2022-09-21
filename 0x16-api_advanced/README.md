# Python | API Advanced:

**Resources:**

* [Reddit API Documentation](https://www.reddit.com/dev/api/#GET_api_v1_me)
* [Query String](https://en.wikipedia.org/wiki/Query_string)

**Learning objectives:**

* How to **read API documentation** to find the endpoints you’re looking for
* How to use an ``API with pagination``
* How to ``parse JSON`` results from an API
* How to make a ``recursive API call``
* How to ``sort a dictionary by value``

**Requirements:**

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* Libraries imported in your Python files must be organized in alphabetical order
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* You must use the ``Requests module`` for sending HTTP requests to the Reddit API

## Environment

* Languages: Python
* Operating System: Ubuntu 20.04 LTS
* Style guidelines: [pycodestyle](https://pypi.org/project/pycodestyle/) - [Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
* Interpreter: python3 (version 3.9)
 > **Note:** The file shoul have executable permissions: ``chmod u+x [filename]`` --> run with ``./filename``

## Description of each file:

| Files          |Desription
|:----------------|:-------------------------------:|
|0-subs.py |Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
|1-top_ten.py |Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
|2-recurse.py |Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
|100-count.py |Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

## Authors

* [Agustin Flom](https://github.com/agusfl)
