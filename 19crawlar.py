#cookie 
    # 網站存放在瀏覽器的一小段內容
    #連線時,放在request headers 中送出
    #ctrl+shift+i  -->application-->cookies 在website 裏 再回到network
#追蹤超連結 - 連續抓取頁面

import urllib.request as req
def getdata(url):

    request=req.Request(url,headers={
        'cookie':'over18=1', #因為要這個cookie 才更是一個users 應有的性質(因為進入website要回答這問題)
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    })
    with req.urlopen(request) as response:
        data=response.read().decode('utf-8')
    #用BS4做解釋
    import bs4
    wholepage=bs4.BeautifulSoup(data,'html.parser')
    topic=wholepage.find_all('div',class_='title')
    for title in topic:
        if title!=None:
            print(title.a.string) 
    #抓取到上一頁的連結       
    nextpage=wholepage.find('a',string='‹ 上頁') #找到內文是‹ 上頁的a 標籤,從以抓取到上一頁的連結
    #print(nextpage['href']) #因為我們想找到/bbs/movie/index8972.html 來進行連結,以他的重要字串前是href
    return(nextpage['href']) #本來上面這固是找到得,但因為我們想找多頁的結果,便要改用return顥示一個結果
#主程序:負責抓取多個頁面的標題:
PageUrl='https://www.ptt.cc/bbs/Gossiping/index.html' #建立一個變數
#getdata(PageUrl) #1,呼叫函式 ,函式裏面的是呼叫PageUrl.為什麼用函式,因為要抓取很多頁面 
#PageUrl=getdata(PageUrl)#2,由放上面以改用return來生結果所以,即要放入結果值即:PageUrl=
count=0 
while count<=3: #因為要找的頁數是下邊這個link,因為下邊的link 要縮排.這裏也是填寫找幾頁的要求
    PageUrl='https://www.ptt.cc'+getdata(PageUrl) #3,要再加上'https://www.ptt.cc'
    count+=1
#print(PageUrl) #因為有上面第三項的改動,這部分便要刪除,改成一個迴轉要抓多少頁就是count 和 while 上面部分

#第一加了cookie
#第二用了函式包裹了url來怎樣的資料要抓到,而且要BS4多頁抓 a 內文的標X,然後用return 反回結果