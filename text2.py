import urllib.request
import ssl
import chardet
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen("https://tieba.baidu.com/index.html")
html = response.read()
chardit1 = chardet.detect(html)
print(chardit1)
print(html.decode(chardit1['encoding']))