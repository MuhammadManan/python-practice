'''#  working with requests library
import requests

Response = requests.get("https://api.github.com/users/octocat")
# print(Response)
# print(Response.text)

with open("octocat.json", "w") as file:
    file.write(Response.text)'''


# working with re module
# import re
# text = "The quick lazy brown fox jumps over the lazy dog."
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found:", match.group())
#     print(match.start())
#     print(match.end())
# else:
#     print("No match found.")

# matches = re.findall("the", text, re.IGNORECASE)
# print("Matches found:", matches)
# if matches:
#     print("Number of matches:", len(matches))
#     for match in matches:
#         print("Match:", match)


# replace_text = re.sub("lazy", "active", text)
# print("Replaced text:", replace_text)
# if you want to replace all occurrences of a word, use re.sub



# Working with multithreading
import threading 
import time

def worker(num):
    print(f"Worker {num} is starting")
    time.sleep(2)
    print(f"Worker {num} has finished")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All workers have finished execution")