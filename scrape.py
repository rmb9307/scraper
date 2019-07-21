from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

## match = soup.title.text
## match = soup.find('div')
## match = soup.find('div', class_='footer').text

## print(match)

article = soup.find('div', class_='article')
# headline = article.h2.a.text ## html elements can be accessed by simple dot notation
# summary = article.p.text
# print('headline: ', headline, ' | summary: ', summary)

## find_all ##
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text ## html elements can be accessed by simple dot notation
    summary = article.p.text
    # print('headline: ', headline, ' | summary: ', summary)

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())