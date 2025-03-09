#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
import requests
import re
from collections import Counter

def count_words(subreddit, word_list, counts=None, after=None):
    """Recursively fetches hot article titles and counts occurrences of keywords."""
    if counts is None:
        counts = Counter()
    
    if not subreddit or not isinstance(subreddit, str) or not word_list:
        return
    
    word_list = [word.lower() for word in word_list]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "API Practice (by u/yourusername)"}
    params = {"limit": 100, "after": after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            
            for post in posts:
                title = post["data"].get("title", "").lower()
                words = re.findall(r'\b\w+\b', title)
                for word in words:
                    if word in word_list:
                        counts[word] += 1
            
            after = data.get("data", {}).get("after")
            if after:
                return count_words(subreddit, word_list, counts, after)
            else:
                sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    if count > 0:
                        print(f"{word}: {count}")
    except requests.RequestException:
        return
