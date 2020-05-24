#封包用來整理,分類模組程式
#專案檔案配置
#專案資料夾
    #-主程式.py  (main.py)
    #-封包資料夾  (geometry)
        # __init__.py  (一定要用這個檔案名稱來確定這是一個封包package 的module 模組,不然沒用)
        # 模組一.py     (point.py)
        # 模組二.py     (line.py)

#基本語法
#import 封包的名稱.模組名稱 或建立別名如下
#import 封包的名稱.模組名稱 as 模組別名

import geometry_1.point               #直接用原名呼叫出來
result=geometry_1.point.distance(3,4)  #兩個寫法也可以,先運計變成一個值,再印出來
print(result)

import geometry_1.line as line   #已改了別名再作運算
print(line.slope(1,1,3,3))  #或者直接把運算印出來