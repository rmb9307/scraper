from bs4 import BeautifulSoup
import requests
import csv 

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')


# match = soup.title.text
# match = soup.find('div')
# match = soup.find('div', class_='footer').text
# print(match)

# ------> html elements can be accessed by simple dot notation, more specific attributes
#         can be accessed with .find method

# article = soup.find('div', class_='article')
# headline = article.h2.a.text
# summary = article.p.text
# print('headline: ', headline, ' | summary: ', summary)

## find_all ##
# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text ## html elements can be accessed by simple dot notation
#     summary = article.p.text
    # print('headline: ', headline, ' | summary: ', summary)

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text

    summary = article.find('div', class_='entry-content').p.text

    try: 
        video_source = article.find('iframe', class_='youtube-player')['src']
        video_id = video_source.split('/')[4]
        video_id = video_id.split('?')[0]

        youtube_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        youtube_link = None

    print(headline, ': ', youtube_link)
    print()

    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()