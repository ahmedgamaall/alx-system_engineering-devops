#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit)"""
import requests


def number_of_subscribers(subreddit):
    """Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects"""

    headers = {'User-Agent': 'Chrome/6.0'}
    request = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers=headers)

    if request.status_code == 200:
        subscribers = request.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
