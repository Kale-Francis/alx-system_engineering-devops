#!/usr/bin/python3
import requests
from collections import Counter

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers of a given subreddit.
    Returns:
        - Number of subscribers if subreddit is valid.
        - 0 if subreddit is invalid or not found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "API-Advanced-Task"}  # Custom User-Agent to avoid Too Many Requests error
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

def top_ten(subreddit):
    """
    Queries the Reddit API to get the titles of the first 10 hot posts in a subreddit.
    Prints the titles or 'None' if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "API-Advanced-Task"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        for post in posts:
            print(post["data"].get("title"))
    else:
        print("None")

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve all hot post titles for a subreddit.
    Returns a list of titles, or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "API-Advanced-Task"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    for post in posts:
        hot_list.append(post["data"].get("title"))
    
    after = data.get("data", {}).get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    
    return hot_list

def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively queries the Reddit API to count occurrences of keywords in hot post titles.
    Prints sorted word occurrences in descending order.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "API-Advanced-Task"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    for post in posts:
        title = post["data"].get("title", "").lower().split()
        for word in word_list:
            word_count[word.lower()] = word_count.get(word.lower(), 0) + title.count(word.lower())
    
    after = data.get("data", {}).get("after")
    if after:
        return count_words(subreddit, word_list, word_count, after)
    
    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")

