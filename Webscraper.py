from bs4 import BeautifulSoup
import requests
import pandas as pd

Websites = pd.read_csv (r'/Documents/Coding projects/Caravan Park Websites.csv')
print(websites)
html_text = requests.get('https://www.campsitephotos.com/rv-campground/ca/angels-camp-rv-camping-resort/').text
soup = BeautifulSoup(html_text)
address = soup.find('address').text
print(address)
#commentto test
