import requests
import os
from bs4 import BeautifulSoup

os.chdir("C:/Users/aidan/Documents/GitHub/username-checker/src/py")

base = "https://github.com/"

fi = open("wordlist.txt", "r")
fl = open("valid-gh.txt", "a")

for i in fi:
    url = base + i.strip()
    page = requests.get(url)

    print("trying: " + i.strip() + "\n")

    if "Not Found" in page.text:
        print("FOUND printng: " + i.strip() + "\n")
        fl.write(i.strip()+"\n")
        

fi.close()
fl.close()