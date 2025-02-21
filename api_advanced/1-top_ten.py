#!/usr/bin/python3
"""Module to query Reddit API and get top 10 hot posts of a subreddit"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit"""
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Reddit API URL for hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    try:
        # Make GET request to Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if subreddit exists
        if response.status_code == 404:
            print("None")
            return
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json().get('data', {}).get('children', [])
            
            # Print titles of first 10 posts
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print("None")

    except Exception:
        print("None")
