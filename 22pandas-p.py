#Pandas -Series 多種應用
#1.自訂索引-語法如下 -data.index
    #import pandas as pd
    #data=pd.Series(資料列表,index=索引列表)
    #print(data.index)
#2.資料型態-語法如下 -data.dtype
    #import pandas as pd
    #data=pd.Series(資料列表)
    #print(data.dtype)   #印出dtype屬性
#3. 資料數量-語法如下-data.size
    #import pandas as pd
    #data=pd.Series(資料列表)
    #print(data.size) #列印size 屬性
#4. 根據順序取值-語法如下 -data.[] 
    #import pandas as pd
    #data=pd.Series (資料列表)
    #print(data.[1]) (取得資料順序),例子裏放[1],實際是第二筆資料,因為是從0開始
#5  根據索引取值- 語法如下 - data[索引](索引是可以自我定義,數字串或文字串)
    #import pandas as pd
    #data=pd.Series(資料列表,index=索引列表)
    #print(data[索引])
#6  數字運算 - 一些指令
    # data.sum()加法總和,data.max()最大值,data.prod()乖法總和
    # data.mean()算平均數 ,data.median() 中位數,data.std() 標進差, 
    # data.nlargest(3) 最'大值的,()是變數,例如現在是(3)即表示取最前3大的數值. 
    # data.nsmallest(2)最小值的,()是變數,例如現在是(2)即表示取最前2小的數值.
#7   字串運算-一些指令,各種指串操作,都定義在str 底下
    #data.str.lower()把所有字串變成小寫, data.str.upper()把所有字串變成大寫, data.str.len()字串合共長度,
    #data.str.cat(sep=',') 把所有的字串串在一起,','逗號是可以改別的 , data.str.contains('P') 來判斷字串裏包含什麼,像(P)就是看字串裏有含P,這個字嗎
    #data.str.replace('你好','hello') 取代字串,後邊的變量取代前面的,例子裏用Hello 取代 你好