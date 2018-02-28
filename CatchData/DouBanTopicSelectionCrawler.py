# -*- coding:utf-8 -*-
import urllib.request as urlrequest
from bs4 import BeautifulSoup

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')         #改变标准输出的默认编码

doubantopicselection300_url = "https://www.douban.com/group/explore?start={}"

with open('doubantopicselection250.txt', 'w',encoding='utf-8') as outputfile:
    for i in range(10):
        start = i * 30
        url_visit = doubantopicselection300_url.format(start)
        crawl_content = urlrequest.urlopen(url_visit).read()
        http_content = crawl_content.decode('utf8')
        #print(http_content)
        soup = BeautifulSoup(http_content, 'html.parser')
        #print(soup.prettify())
        all_item_divs = soup.find_all(class_='channel-item')

        for each_item_div in all_item_divs:
            #print(each_item_div.prettify())
            pic_div = each_item_div.find(class_='bd')
            likes_div = each_item_div.find(class_='likes')
            #print(pic_div.prettify())
            item_href = pic_div.find('a')['href']
            item_name = pic_div.find('a').string
            item_likes = likes_div.text
            #item_name = pic_div.find('img')['alt']

            #print('{}{}'.format(item_href,item_name))
            outputfile.write('{}{}  {}\r\n'.format(item_href,item_name,item_likes))