#import 基本語法
# import 模組名稱(module) --形式一
#import 模組名稱 as 模組別名  --形式二
#呼叫的/使用法如下:
# 模組名稱或別名.函式名稱(變數資料) - 方式一
#模組名稱或別名.變數名稱           - 方式二
#內建模組-例如Sys 


#載入內建的sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

#建入geomotry 模組,載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slop(1,2,5,6)
# print(result)

#調整搜尋模組的路徑
# import sys
# print(sys.path) #安照這路徑來搜尋模組,要是超了這個範圍便找不到了
import sys
sys.path.append('module') #可以自定新路徑,所以模組放到別的地方也可以呼叫使用
# print(sys.path)
import geometry
print(geometry.distance(1,1,5,5))


