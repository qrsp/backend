import requests
from bs4 import BeautifulSoup

def ptt_crawler(name, page):
    home = 'https://www.ptt.cc'
    url = home + '/bbs/' + name + '/index.html'
    
    while page > 0:
        page -= 1
        response = requests.get(url, cookies={'over18': '1'})
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.select('title')[0]
        print('看板名稱: ' + title.getText())

        # last page
        url = home + soup.select('.btn ~ .wide')[0].attrs['href']
        
        links = soup.select('.title > a')
        authors = soup.select('.author')
        dates = soup.select('.date')


        for i in range(len(links)):
            print('作者: ' + authors[i].getText())
            print('日期: ' + dates[i].getText())
            print('標題: ' + links[i].getText())

            content_link =  home + links[i].attrs['href']
            content_response = requests.get(content_link, cookies={'over18': '1'})
            soup = BeautifulSoup(content_response.text, 'html.parser')

            context = soup.select('#main-content')[0]
            print('內文: ' + context.getText())
        
    

ptt_crawler('Python', 2)