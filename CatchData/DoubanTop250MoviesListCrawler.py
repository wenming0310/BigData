# -*- coding:utf-8 -*-
import urllib.request as urlrequest
from bs4 import BeautifulSoup
top250_url = "https://movie.douban.com/top250?start={}&filter="

with open('douban_250.txt', 'w') as outputfile:
    for i in range(10):
        start = i * 25
        url_visit = top250_url.format(start)
        crawl_content = urlrequest.urlopen(url_visit).read()
        http_content = crawl_content.decode('utf8')
        #print(http_content)
        soup = BeautifulSoup(http_content, 'html.parser')
        #print(soup.prettify())
        all_item_divs = soup.find_all(class_='item')

        for each_item_div in all_item_divs:
            #print(each_item_div.prettify())
            pic_div = each_item_div.find(class_='pic')
            #print(pic_div.prettify())
            item_href = pic_div.find('a')['href']
            item_name = pic_div.find('img')['alt']
            #print('{}{}'.format(item_href,item_name))
            outputfile.write('{}{}\r\n'.format(item_href,item_name))