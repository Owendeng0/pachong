import random
import requests
import re

header = [{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400'},{'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}]


def get_url(url):
    req = requests.get(url,headers = header[random.randint(0,1)])
    result = req.content
    result = result.decode('gbk')
    res = r'<dd class="col-md-3"><a href=(.*?) title='
    list_url = re.findall(res,result)
    list_url_ = []
    for url_ in list_url:
        if '"' in url_:
            url_ = url_.replace('"','')
            url_ = url_.replace('"','')
            list_url.append("https://www.biqukan.cc/book/40164/" + url_)
        elif "'" in url_:
            url_ = url_.replace("'", '')
            url_ = url_.replace("'", '')
            list_url.append("https://www.biqukan.cc/book/40164/" + url_)
    return  list_url


for url_txt in get_url('https://www.biqukan.cc/book/40164/'):
    get_url(url_txt)
