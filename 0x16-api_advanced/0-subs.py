#!/usr/bin/python3
"""a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit)"""
import requests


def number_of_subscribers(subreddit):
    """Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'SubsPythonScript/2.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
