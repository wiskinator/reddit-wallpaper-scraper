import requests
import sys

base_url = "https://reddit.com/"


def get_hot(subreddit):
    subreddit = "r/" + subreddit
    api_string = "/hot"
    full_url = base_url + subreddit + api_string
    params = {"g": "GLOBAL", "count": 1}
    r = requests.get(full_url, params=params)
    return r.content


def main():
    print "This is RWS"
    print get_hot("wallpapers")

    

if __name__ == "__main__":
    sys.exit(main())
