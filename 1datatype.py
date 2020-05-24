#資料的基本單位
#數字
12345
3.5

#字串
'你好嗎'
'HELLO'

#布林值
True
False

# 有順序,可動的列表 LIST
[3,4,5] #先開中刮號再放入數值/字串,就稱列表,列表類似容器
['HELLO']

#有順序,不可動的列表 Tuple
(3,4,5) # 是用刮號
('HELLOE')

# 集合 set ,可以沒順序
{3,4,5}#用大刮號,可以沒順
{'HELLO'}

#字典 Dictionary
{'apple':'蘋果','Happy':'快樂'}  #用逗號隔開

#變數,是用來儲資料的自訂名稱, 而且一定要用英文開頭
#變數名稱=資料
val=(1,2,3) # 這VAL的資料便是3
#print (資料)
print (val)
val=True #上面雖然是VAL=字串(1,2,3),但因為同一VAL在這裏是等於TRUE,所以會取代以顯示
print (val)
val ='Hello'
print (val)
val ={3,4,5}
print (val)