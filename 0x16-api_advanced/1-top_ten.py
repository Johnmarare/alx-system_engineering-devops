#!/usr/bin/python3
"""Query reddit api for top 10 hot posts"""
import requests


def top_ten(subreddit):
    """top 10 hot posts
    return titles else 0
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/John_Marare)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False).json()
    children = response.get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")
