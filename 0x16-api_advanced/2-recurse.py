#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches hot article titles from a given subreddit."""
    if not subreddit or not isinstance(subreddit, str):
        return None
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "API Practice (by u/yourusername)"}
    params = {"limit": 100, "after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            for post in posts:
                hot_list.append(post["data"].get("title"))
            
            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
