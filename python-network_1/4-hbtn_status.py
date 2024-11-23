#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
This script demonstrates the use of the requests package to make
an HTTP GET request and display the response in a specific format.
"""
import requests


if __name__ == "__main__":
    try:
        url = "https://alu-intranet.hbtn.io/status"
        response = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
    except requests.exceptions.RequestException:
        # If there's an error with the ALU URL, try the alternate URL
        url = "http://0.0.0.0:5050/status"
        response = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
