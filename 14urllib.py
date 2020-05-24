#網絡連線
    #載入模組
    #下載特定網址資料 --import urllib.request/ request.urlopen
    #import urllib.request as request #載入urllib 的rquest ,再改別名為request
    #with request.urlopen(網址) as respone:
        #data=respone.read()
    #print (data)
    #例如要找公開資料,便要確認資料格式(json,csv,或其它格式)
    #如果文件是json 檔案便要解讀json 格式,即使用內建的json 模組
#--------------------------------------------------------------#練習開始

#網絡連線
# import urllib.request as request
# #src='https://www.ntu.edu.tw/'
# with request.urlopen('https://www.ntu.edu.tw/') as respone:
#     data=respone.read().decode('utf-8') #取得原始碼,(html,css,js),加入decode=('utf-8')是為了顯示中文
# print(data)

import urllib.request as request
import json #因為這文件是json 的格式,所以要import 來
src='https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c'
with request.urlopen(src) as respone:
    #data=respone.read().decode('utf-8') #取得原始碼,(html,css,js),加入decode=('utf-8')是為了顯示中文
    data=json.load(respone) #利用json 模組處理json 資料格式
#取得公司名稱列表出來
clist=data['result']['results'] #'result' 對應後文件後面全部資料用{}大刮號起來的,'results' 對應後面所有{'公司地址':'北市6樓','ADDR_X':'30002'}等的資料 
with open('company.txt',mode='w',encoding='utf-8') as file:
    #print(clist) #己變了列表資料了
    for company in clist:       #由於每筆資料單獨存在,雖然每筆都是字典1對1,但不能直接輸出,所以用for 迴圈
        file.write(company['公司地址']+'\n') #company 分別是每一筆資料, company = 第一筆資料時,輸出"公司名稱"對應的value,company =第二筆資料時,輸出該筆資料"公司名稱"對應的value. 一直到每一筆資料代入到company 後,for 就結東

