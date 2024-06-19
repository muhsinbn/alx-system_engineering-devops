#!/usr/bin/python3
# This function queries the Reddit API and returns the no. of subscribers

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a custom User-Agent to prevent Too Many Requests error
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0

# Test the function
subreddit = 'learnpython'
print(f"The number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")
