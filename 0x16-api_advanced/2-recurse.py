#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

- Prototype: def recurse(subreddit, hot_list=[])
- Note: You may change the prototype, but it must be able to be called with
just a subreddit supplied. AKA you can add a counter, but it must work without
supplying a starting value in the main.
- If not a valid subreddit, return None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are not following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the
function! This /can/ be done with a loop but the point is to use a recursive
function. :)
"""
import requests