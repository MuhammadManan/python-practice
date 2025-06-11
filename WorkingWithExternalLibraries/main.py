#  working with requests library
import requests

Response = requests.get("https://api.github.com/users/octocat")
# print(Response)
# print(Response.text)

with open("octocat.json", "w") as file:
    file.write(Response.text)