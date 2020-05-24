# import urllib.request as req
# url='https://www.ptt.cc/bbs/movie/index.html'
# request=req.Request(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
# })
# with req.urlopen(request) as repsonse:
#     data=repsonse.read().decode('utf-8')

# import bs4
# wholepage=bs4.BeautifulSoup(data,'html.parser')
# topic=wholepage.find_all('div',class_='title')
# for i in topic:
#     if i !=None:
#         print(i.a.string)

import urllib.request as req
url='https://www.ptt.cc/bbs/movie/index.html'
request=req.Request(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
})
with req.urlopen(request) as response:
    data=response.read().decode('utf-8')

import bs4
wholepage=bs4.BeautifulSoup(data,'html.parser')
topic=wholepage.find_all('div',class_='title')
for title in topic:
    if title!=None:
        print(title.a.string)