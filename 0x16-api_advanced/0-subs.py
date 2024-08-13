#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given
subreddit. If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    request = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers=headers,
        )

    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
