import urllib.request as urlrequest
url_visit = 'https://api.douban.com/v2/movie/26387939'
crawl_content = urlrequest.urlopen(url_visit).read()
print(crawl_content.decode('unicode-escape'))