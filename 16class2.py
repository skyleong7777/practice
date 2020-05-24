#class 第二種應用形式 (類別與實體物件,實體屬性)
    #要先建立實體物件,然後才能使用實體屬性
    #基本語法以下:
    #class 類別名稱:
        #def __init__(self):   #透過操作self 來定義實體屬性
    #建立實體物件,放入變數obj 中
    #obj=類別名稱()   #呼叫初始化函式

    #建立實體物件
    # class point:
    #     def __init__(self,x,y):
    #         self.x=x
    #         self.y=y
    #建立實體物件
    #建立時,可直接傳入參數資料
    # p=point(1,5)

    #使用實體,基本語法如下
    #實體物件.實體屬性名稱 (p.x) p 是實體物件. x屬性名稱
    #p=point(1,5)
    #print(p.x+p.y)
#---------------------------------------------------------#練習開始
# class point: #這例子靠中間def 來運計,然後print 出答案
#     def __init__(self):
#         self.x=3
#         self.y=4
# p1=point()    #class 類別可以重複代入不同物件即object
# print(p1.x,p1.y)
# p2=point()
# print(p1.x,p1.y)

class point: #這例如相反,把運算的過程先設計好,再由下邊呼叫物件和參數再作變化
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=point(3,4)    #class 類別可以重複代入不同物件即object
print(p1.x,p1.y)
p2=point(5,6)
print(p2.x+p2.y)

#例子三
class fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
fname1=fullname('sky','leong')
print('this name is',fname1.first,fname1.last)

fname2=fullname('zero','wong')
print(fname2.first,fname2.last)
