#class 第一種用法 (類別與類別屬性)
# 基本語法如下:
    #定義封裝的變數
    #定義封裝的函式 
    #例子如下: 
    #class test: 定義test類別
        #x=3    #定義變數
        #def say(): #定義函式
            #print('hello')
#如何使用類別
#基本語法如下:
    #類別名稱.屬性名稱
#-----------------------------------------#練習開始
#定義類別,與類別屬性 (封裝在類別中的變數和函式)
# class IO:
#     supportsrc=['console','file']
#     def read(src):
#         if src not in IO.supportsrc:
#             print('not support')
#         else:
#             print('correct',src)
# # 如何使用上面的類別
# print(IO.supportsrc)
# IO.read('file')
# IO.read('internet')

class io:
    message=['happy','sad']
    def read(msg):
        if msg not in io.message:
            print('not here')
        else:
            print('u got it')

io.read('test')
io.read('happy')


