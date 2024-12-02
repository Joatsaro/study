import requests
from bs4 import BeautifulSoup


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
data = requests.get("https://rahulshettyacademy.com/AutomationPractice/", headers=headers)
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())
moviesTable = soup.find('table', {'class':'table-display'})
# print(moviesTable.prettify())
rows = moviesTable.findAll('tr')
# print(rows)
for row in rows[1:]:
    final = row.findAll('td[1]')
    print(final.text)
    # subUrl = row.a['href']
    # subData = requests.get("https://imdb.com"+subUrl, headers=headers)
    # childSoup = BeautifulSoup(subData.content, 'html.parser')
    # if childSoup.find('div', {'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base'}) :
    #     genreZone = childSoup.find('div', {'class':'ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base'})
    #     if genreZone.findAll('li', {'role':'presentation'}):
    #         genreTag = genreZone.findAll('li', {'role':'presentation'})
    #         for genre in genreTag:
    #             print(genre.a.text)
