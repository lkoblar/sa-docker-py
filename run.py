import requests
from helper import hello

print("starting..")
hello()

r = requests.get("https://api.github.com")
print("Status API:", r.status_code)
