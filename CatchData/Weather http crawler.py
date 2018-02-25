import urllib.request as urlrequest
from bs4 import BeautifulSoup
weather_url = 'http://www.weather.com.cn/weather/101010100.shtml'
web_page = urlrequest.urlopen(weather_url).read()
#print(web_page)
soup = BeautifulSoup(web_page, 'html.parser')
#print(soup.find(id = '7d'))
#print(soup.find(id = '7d').get_text())

#forecast_text = soup.find(id = '7d').get_text()
#print(forecast_text.split('\n'))

#print(soup.find(id = '7d'))
#print(soup.find(id = '7d').prettify())  #格式化输出
soup_forecast = soup.find(id = '7d')
soup_forecast_list = soup_forecast.find_all(class_ = 'sky')
for i in range(7):
    x = soup_forecast_list[i].get_text()
    print("{}".format(x))