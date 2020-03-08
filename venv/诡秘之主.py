import random
import requests
import re


header = [{'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400'},{'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}]

req1 = requests.get('https://www.biqukan.cc/book/40164/23067320.html',headers = header[random.randint(0,1)])
req2 = requests.get('https://www.biqukan.cc/book/40164/23067320_2.html',headers = header[random.randint(0,1)])
result1 = req1.content
result1 = result1.decode('gbk')
result2 = req2.content
result2 = result2.decode('gbk')
title_re = re.compile(r' <li class="active">(.*?)</li>')
text_re = re.compile(r'<br><br>([\s\S]*?)</div>')
title = re.findall(title_re,result1)
text1 = re.findall(text_re,result1)
text2 = re.findall(text_re,result2)
title = title[0]
print(title)
text1.append(text2[0])
text1 = '\r\n'.join(text1)
text1 = text1.split('\r\n')
text_1 = []
for sentence in text1:
    sentence = sentence.strip()
    if '&nbsp;&nbsp;&nbsp;&nbsp;' in sentence:
        sentence = sentence.replace('&nbsp;', '')
    if ' ' in sentence:
        sentence = sentence.replace(' ','')
        if '<br/'>'' in sentence:
            sentence = sentence.replace('<br/>','')
            text_1.append(sentence)
        else:
            text_1.append(sentence)
    elif '<br/>' in sentence:
        sentence = sentence.replace('<br/>','')
        text_1.append(sentence)
    elif '-->><p class="text-danger text-center mg0">本章未完，点击下一页继续阅读</p>' in sentence:
        sentence = sentence.replace(r'-->><p class="text-danger text-center mg0">本章未完，点击下一页继续阅读</p>', '')
        text_1.append(sentence)
    else:
        text_1.append(sentence)
count = text_1.count('')
for i in range(count):
    text_1.remove('')
for sentence in text_1:
    print(sentence)