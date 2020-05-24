#基本語法以下 如何用python open 其它文件
    # 檔案物件= open (檔案路徑,mode=開啟模式)
#開啟模式:R讀/W寫/R+讀和寫 
#讀取全部文字的語法如下:
    #檔案物件.read()
#讀取一行一行的語法如下:
    # for 變數 in 檔案物件:
        #從檔案依次序讀取每行文字到 變數 中
#讀取JSON 格式,語法如下:
    #import json
        #讀取到的資料=json.load(檔案物件)
#寫入json 格式,語法如下:
    #import json
        #json.dump(要寫入的資料,檔案物件)
#寫入文字,語法如下
    #檔案物件.write(字串)
    #檔案物件.write(字串\n) \n 是換行的意思
#關閉語法,如法有兩種
    #檔案物件.close()  #方法一
    #with open(檔案路徑,mode=開啟模式) as 檔案物件      #方法二推介,因為這區塊會自動,安全的關閉檔案
        #讀取或寫入檔案的程式
#--------------------------------------------------# 開始練習
#儲存檔案
# file=open('data.txt',mode='w') #開啟
# file.write('this is my file\nSecond line')  #操作
# file.close                     #關閉

# file=open('data.txt',mode='w',encoding='utf-8') #開啟,encoding 是可以處理文字上的編碼,utf-8 這樣中文便可以處理了
# file.write('中文字測試\nSecond line')  #中文操作測試
# file.close  
# Best way to open a file
# with open('data1.txt',mode='w',encoding='utf-8') as file:
#         file.write('5\n3')
# # 讀取檔案
# #將上面的5和3,一行行讀取出來,並計算總合
# sum=0
# with open('data1.txt',mode='r',encoding='utf-8') as file:
#     #print(file.read()) #我自己寫的
#     for line in file:
#         sum+=int(line) #把它變成整數印出來
#         #data=file.read()
# print(sum)  #老師用的

# 使用json 格式讀取,複寫檔案
# import json
# with open('config.json',mode='r') as file:
#     data=json.load(file)
# print('test Name',data['name'])
# print('test Name',data['name'])
#更新json 資料,例字如下: 
import json
with open('config.json',mode='r') as file:   
        data=json.load(file)
#print (data)
data['name']='latest name'
with open('config.json',mode='w') as file:
    json.dump(data,file)    


