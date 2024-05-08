#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should
not)."""
import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    """Invalid subreddits may return a redirect to search results.
    Ensure that you are NOT following redirects"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Chrome/6.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        for i in range(100):
            title = response.json()["data"]["children"][i]["data"]["title"]
            for word in word_list:
                if word.lower() in title.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        after = response.json()["data"]["after"]
        if after is None:
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                if value != 0:
                    print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dict)
    else:
        return
