#!/usr/bin/python3
"""
Fetches a URL and displays the response body using the requests module.
"""

import requests

def fetch_status(url):
    """Fetches the status of a given URL and prints its type and content."""
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch_status(url)

