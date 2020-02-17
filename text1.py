import requests
from lxml import etree
import time
#爬取豆瓣电影 神秘巨星
#headers={'user-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400'}
#url = 'https://movie.douban.com/subject/26942674/'
#data = requests.get(url,headers=headers).text
#s = etree.HTML(data)

#film_name = s.xpath('//*[@id="content"]/h1/span[1]/text()')
#print("电影名",film_name)

#爬取豆瓣图书top250
for i in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(i*25)
    data = requests.get(url).text
    f = etree.HTML(data)
    books = f.xpath('//*[@id="content"]/div/div[1]/div/table')
    for div in books:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        comment = div.xpath('./tr/td[2]/p[2]/span/text()')
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip('(').strip().strip(')')
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0]
        time.sleep(1) #加个睡眠，防止IP被封

        if len(comment)>0:
            print('{}-->{}-->{}-->{}-->{}'.format(title,score,comment[0],num,href))
        else:
            print('{}-->{}-->{}-->{}'.format(title,score,num,href))
        print('\n')

