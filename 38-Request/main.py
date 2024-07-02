import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.google.com/")


soup = BeautifulSoup(response.text, 'html.parser')

for anchor in soup.find_all("a"):
    print(anchor)   