#如何用python 來取得web site 裏的html 資料, 那就要運用到第三插件-beautifulsoup commend: pip install beautifulsoup4
#python 裏有一毎叫pip 套件管理工具
#為了模擬是一個user,可透過web site 裏的ctrl+shift+i 來找出'開發人員工具的'->network->reflesh->index.html->header->request header->user agent->copy 以下字串
import urllib.request as req #抓取ptt 電影版的網頁版原始碼(html)
url='https://www.ptt.cc/bbs/movie/index.html'
#建立一個request 物件,附加request headers 的資訊,因為要摸仿一個user 行為
request=req.Request(url,headers={  #Request 的R 一定要大草R
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
})
with req.urlopen(request) as response: #因為變量是request 了,所以用這裏面的特性來打開web site
    data=response.read().decode('utf-8')
#print(data)

#解折原始碼,收得每篇文章的標題
#因為這是html,要安裝beautifulsoup4 即pip install beautifulsoup4,簡稱bs4
import bs4
root=bs4.BeautifulSoup(data,'html.parser') #data 是上面剛read 到的 html data,透過bs4 來解釋,parser是解折器的意思
#print(root.title.string) #root 指全份文件,title 指目標,srting 後面的文字
#titles=root.find('div',class_='title'), #find 這個功能是bs4 裏面的功能,用來尋找你所打的字串的'其中符合一個',因為這裏的目標都是用div,和class_='titles',單純class 是python的保留字,程式中是不能使用,所以BS4就選擇使用class_來籂選標籤中的class屬性
abc=root.find_all('div',class_='title')
#print(titles) #因為titles 含有其它字串, 要是只字標題應如下更改:titles.a.string 即是只印出a 後的字串
#print(titles)
for title in abc:
    if title.a !=None:
        print(title.a.string)

