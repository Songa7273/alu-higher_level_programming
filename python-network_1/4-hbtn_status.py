#!/usr/bin/python3
"""
Script that fetches a status URL using requests package
"""
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text)
