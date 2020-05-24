#什麼是Pandas? --概念類似'試算表'的資料分拆套件
#項目如下:
    #1.安裝Pandas  pip install pandas
    #2.認識單維度的資料----Series 
        #2.1 就像一個列表(coloum),或是試算表中直向的欄位資料
        #2.2 建立Series 的模組語法如下
            #import pandas as pd   (載入Pandas 模組,然後改個名叫pd)
            #pd.Series(列表)        (以列表資料為底.建立Series)
        #2.3 使用Series 
            #import pandas as pd
            #data = pd.Series(列表)
            #data.max()找到最大值
            #data.median() 找到中位數
            #data=data*2 放大兩倍
    #3.認識雙維度的資料----DataFrame
        #3.1 就像一個表格,有欄(coloum)和列(row)的概念
        #3.2 建立Dataframe 的模組語法如下:
            #import pandas as pd (載入Pandas 模組,然後改個名叫pd)
            #pd.DataFrame(字典)  (以字典資料為底.建立DataFrame)
        #3.3 取得特定欄(直向) 語法如下:
            #import pandas as pd
            #data=pd.DataFrame(字典)
            #data['欄位名稱']
        #3.4 取得特定列(橫向) 語法如下: iloc (ilocation)
            #import pandas as pd
            #data=pd.DataFrame(字典)
            #data.iloc[列編號] #列編號按順序由0開始累加
#--------------------------------------------------------------#練習開始
#載入pandas 模組 Series 練習,記得Series 是用列表啊
# import pandas as pd
# data=pd.Series([20,10,40,100])
# print(data)
# print('Max:',data.max()) #最大值
# print('Median:',data.median())#中位值
# print('Double time:\n',data*2)#兩倍放大
# print('Divede value:\n',data/2)#除兩倍
# #這指令是比較值的運算,看有沒有重覆,兩個等於意思是比較運算,看這個值有沒有在
# data=data==20 #第一個data 是表格的參數,然後在data 裏拿20 和每個數作出比較,有就true,沒就false
# print(data)

#DataFrame 的練習,記得DataFrame 是用字典法啊
import pandas as pd
data=pd.DataFrame({ #先用不可動列表的刮號開(),再用字典的大刮號{},然後表示字典裏的值 key:value
    'name':['Sky','Zero','Aries'],'Salary':[1000,2000,9000] #字典裏的對應文字值有什麼,再用可動列表[]把每個值分開來,
    })
print(data['name']) #取得特定橺位練習

print('---------------------------------')

print(data.iloc[1])

