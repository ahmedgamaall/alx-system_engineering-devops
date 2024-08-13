#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """prints first 10 hot posts"""

    headers = {'User-Agent': 'MyPythonScript/1.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    request = requests.get(
        url=url,
        headers=headers,
        allow_redirects=False,
        )
    if request.status_code == 200:
        hot_ten_posts = request.json().get('data').get('children')
        if not hot_ten_posts:
            return print("None")
        else:
            for post in hot_ten_posts:
                print(post.get('data').get("title"))
    else:
        return print("None")
