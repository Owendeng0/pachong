import urllib.request


url = 'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http':'202.120.38.131:80'})

opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)