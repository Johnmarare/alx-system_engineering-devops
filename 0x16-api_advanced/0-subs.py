#!/usr/bin/python3
"""
queries reddit api to return number of subs for a given subredit
"""
import requests


def number_of_subscribers(subreddit):
    """
    sureddit: to be queried
    Return: Number of subs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/John_Marare)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")

    return results.get("subscribers")
