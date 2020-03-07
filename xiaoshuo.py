import urllib.request,bs4
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#获取页面初始数据
def getHtmlcode(url):
    #写请求头
    user_agent = "user-agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 QQBrowser/3.9.3943.400"
    headers = {"User_agent": user_agent}


    response=urllib.request.Request(url,headers=headers)#发起请求
    result=urllib.request.urlopen(response)
    html=result.read()
    return html

#分析页面

def paarser(url):
    html=getHtmlcode(url)#调用getHtmlcode函数
    soup=BeautifulSoup(html,'html.parser')


    return soup  #返回页面信息

#获取每章目录链接


def Charpter_url(url):
    soup=paarser(url)#调用paarser
    datas=soup.find('div',id="list").find_all('a')
    url_list=[]#新建列表存储地址
    for data in datas:
        page_url='https://www.biquge.net'+data['href']#拼接真实地址
        page_name=data.text#每一章的名字
        url_list.append(page_url)


    return url_list

#获取文章单章正文


def get_Charpter_text(url):
    soup=paarser(url)
    content=soup.find('div',id="content").text
    content1=content.strip().replace("<br/>","")#格式
    return content

#保存文件


def save_text(url):
    url_list=Charpter_url(url)
    num=1
    with open('飞剑问道.text','a',encoding='utf-8') as f:
        for page_url in url_list:
            contents=get_Charpter_text(page_url)
            f.write(contents)


            print('第{}章下载完成'.format(num))
            num+=1

        f.close()


if __name__=='__main__':
    url='https://www.biqudu.net/22_22926/'
    save_text(url)
