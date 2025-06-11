'''#  working with requests library
import requests

Response = requests.get("https://api.github.com/users/octocat")
# print(Response)
# print(Response.text)

with open("octocat.json", "w") as file:
    file.write(Response.text)'''


import re
# working with re module
text = "The quick brown fox jumps over the lazy dog."
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found:", match.group())
#     print(match.start())
#     print(match.end())
# else:
#     print("No match found.")

matches = re.findall("the", text, re.IGNORECASE)
print("Matches found:", matches)
if matches:
    print("Number of matches:", len(matches))
    for match in matches:
        print("Match:", match)