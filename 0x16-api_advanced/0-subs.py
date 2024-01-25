#!/usr/bin/python3
"""
queries reddit api to return number of subs for a given subredit
"""
import requests


def number_of_subscribers(subreddit):
    """sureddit: to be queried
    Return: Number of subs
    """
    if subreddit is None:
        return (0)
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/John_Marare)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    results = response.json()
    subs = results.get("data", {}).get("subscribers", 0)

    return subs
