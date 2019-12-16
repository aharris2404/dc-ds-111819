import requests
from bs4 import BeautifulSoup as bs

URL = "https://washingtondc.craigslist.org/search/apa?sort=date&"

page = requests.get(URL)
soup = bs(page.content, 'html.parser')

price = soup.find_all('span', class_='result-price')[-1].text
print(price)
