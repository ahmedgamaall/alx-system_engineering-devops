#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/6.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        for i in range(10):
            title = response.json()["data"]["children"][i]["data"]["title"]
            print(title)
    else:
        print(None)
