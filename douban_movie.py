import requests
from bs4 import BeautifulSoup
i = 0
url = "https://movie.douban.com/top250"
"""
page 2
https://movie.douban.com/top250?start=25&filter=
page3 
https://movie.douban.com/top250?start=50&filter=
"""
urls = ["https://movie.douban.com/top250?start="+str(n)+"&filter=" for n in range(0, 250, 25)]
for url in urls:
    web_data = requests.get(url)
    # print(web_data)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)
    titles = soup.select('div.hd > a')
    # print(title)
    rates = soup.select('span.rating_num')
    print(rates)

    imgs = soup.select('img[width="100"]')

    for title, rate, img in zip(titles, rates, imgs):
        data = {
            'title': list(title.stripped_strings),
            'rate': rate.get_text(),
            'img': img.get('src')
        }
        i += 1
        # filePath = "C:\Users\qianj\Downloads\python\Download_File"
        fileName = str(i)+"、"+data['title'][0]+" "+data['rate']+"分.jpg"
        pic = requests.get(data['img'])
        with open('C:/Users/qianj/Downloads/python/DownloadFile/'+fileName, 'wb') as photo:
            photo.write(pic.content)
        print(data)
