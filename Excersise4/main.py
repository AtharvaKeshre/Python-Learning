# 2d44a9b160204c399b0e2346225c3c31
import requests
from bs4 import BeautifulSoup
import json

query = input("What type of new you would like to check on : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-05-17&sortBy=publishedAt&apiKey=2d44a9b160204c399b0e2346225c3c31"

r = requests.get(url)
# print(r.text)
news = json.loads(r.text)
# print(news)
i=0
for article in news["articles"]:
    if i == 10:
        exit()
    print(article["title"] + "----" + article["description"]) 
    print("----------------------------------------------")

    i+=1
