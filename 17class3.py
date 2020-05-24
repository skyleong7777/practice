#續上面的class 使用方法,仍然在這一章探討形式二
#但用法加多一種叫:實體方法,如下 (也是這章主要學習的)
#類別與實體物件,實體屬性,實體方法
    #實體屬性是:封裝在實體物件中的'變數' (重溫)
    #emaple:
    #class point:
        #def __init__(self,x,y):
            #self.x=x
            #self.y=y
    #p=point(1,5)
    #print(p.x+py)
    #實體方法 (今章主要學習):封裝在實體物件中的'函式'
    #如下:
    #class 類別名稱:
        #def __init__(self):#定義實體屬性
            #封裝在實體物件中的變數
        #def 方法名稱(self,更多自訂參數):     #定義實體方法/函式    (主要內容在這,他排版跟def 一樣大)
            #方法主體,透過self 操作實體物件 #這個self 可以想成當用自定義的class宣布一個instance,self 就代表邊個邊個instance,只是在定義class時還不會知道之後的instance叫什麼所以先用self表示
    #建立實體物件,放入變數obj 中 
    #obj=類別名稱()
    #基本語法
    #實體物件.實體方法名稱(參數資料) (跟函式呼喚的方式一樣)

#----------------------------------------------------------#練習開始
# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show (self): #定義實體方法
#         print(self.x,self.y)  #對應下面的p.show()  
#     def distance (self,x2,y2):
#         return (((self.x-x2)**2+(self.y-y2)**2)**0.5) #return 用來計算兩點距離
    
# p=point(3,4)  #建立實體,呼叫初始化函式
# #p.show()       #呼叫實體方法/函式 . (要是想印出來便取消注解)
# result=p.distance(0,0) #P.distance(0,0)因為兩個參數,所以這裏就填入兩個參數.為什麼這裏要result,因為上面運來了return 這功能,return 一定帶著結個,所以增加了一個值來儲存在,計以印出答案
# print(result)

#練習二:file 實體物件的設計: 包裝檔案讀取的程式
class file:
    #建立初始化的函式
    def __init__(self,name):
        self.name=name  #name 是從參數進來
        self.file=None      #尚未開啟檔案,初期是0 (沒這個設定self.file=0 後面也可以執行)
    #建立實體方法,以下有open, read 兩種方法
    def open (self):
        self.file=open(self.name,mode='r',encoding='utf-8') #調動python內用的開啟file功能('data....'utf-8')得到一個物件來存入 實體file 裏
    def read(self):
        return self.file.read() #(利用上面得到的物品 file read 把檔案讀取出來再迴轉成結果
#讀取第一個文件
f1=file('data.txt') #建立實體物件
f1.open() #就會跑上面open 的那段coding
result=f1.read() #因為有return,所以要存入結果
print(result)

f2=file('data1.txt')
f2.open()
result=f2.read()
print(result)    

            

