# Task: check if there is a working website at the address
import sys
import requests

website_url = sys.argv[1]
resp = requests.head(website_url)

if resp.status_code == 200:
    print("Website running!")
