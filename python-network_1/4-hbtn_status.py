#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
This script demonstrates the use of the requests package to make
an HTTP GET request and display the response in a specific format.
The script will:
    - Make a GET request to the specified URL
    - Display the response body type
    - Display the response content
"""
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
