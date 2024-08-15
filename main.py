import requests
from os import remove
from bs4 import BeautifulSoup
from config import *

print("How many pages back do you want to go in the /tg/station ban database?")
pages_back = int(input())
URL1 = "https://tgstation13.org/tgdb/publicbans.php"
URL2 = ""
try:
    remove("bans.txt")
except:
    pass
database_file = open("bans.txt", "x")
def ban_scrape(URL, URL2):
    x = pages_back
    while x >0:
        x-= 1
        URL = URL1+URL2
        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")
        banned = soup.findAll("b")
        isBanned = ""
        primed = False
        for ban in banned:
            if(ban.text == "Active"):
                pass
            elif(ban.text == "Server"):
                pass
            elif(ban.text== "Unbanned"):
                isBanned = "Unbanned"
            else:
                if isBanned == "Unbanned":
                    isBanned = ban.text
                else:
                    print(isBanned)
                    database_file.write(isBanned)
                    database_file.write('\n')
                    isBanned = ban.text
        next = BeautifulSoup(page.text, "html.parser")
    
        for a in next.find_all('a', href=True):
            if("?beforeid" in a['href']):
                URL2 = a['href']
        
ban_scrape(URL1, URL2)

input()