import requests
import os
from bs4 import BeautifulSoup

os.chdir("C:/Users/aidan/Documents/GitHub/username-checker/src/py")

base = "https://steamcommunity.com/id/"

fi = open("wordlist.txt", "r")
fl = open("valid-steam.txt", "a")

for i in fi:
    url = base + i.strip()
    page = requests.get(url)

    print("trying: "+ i)

    if "The specified profile could not be found." in page.text and len(i.strip()) > 1:
        print("FOUND, id: " + i)
        fl.write(i.strip()+"\n")

fi.close()
fl.close()
