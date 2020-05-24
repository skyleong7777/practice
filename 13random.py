#Random 
# 1,隨機選取 --choice & sample
    # import random 
        #ramdom.choice([0,1,5,8]) 從列表中隨機取 1 個資料
        #ramdom.sample([0,1,5,8],2) 從列表中隨機取n 個資料,例如現在最後是2,就是兩個,3就是3個,但不能超過5個,因為這裏最多只有4個數值
#2,隨機調換順序 --shuffle
    # import random 
        #data=[0,1,5,8]       
        #random.shuffle(data)  只要執行shuffle,列表的資料<就地>隨機調換次序
        # print(data)
#3,隨機亂數-- random, uniform 隨機出現的數值機率一樣
    #import random 
        #random.random()  random 是標準取得0 至1 之間的隨機亂數
        # random.uniform(0.0,1.0)    是標準取得0.0 至1.0 之間的隨機亂數

#4,常態分配亂數--normalvariate(統計學常用到的)
    #import random 例子:#取得"平均數"是100,"標準差是"10的. #常態分配亂數,所以結果的數值一般會在(x+Y)和(x-y)附近
        #random.normalvariate(100,10) , #random.normalvariate(x,y) 
        

#Statistics 載入模組 
#1,計算平均數--mean
    #import statistics
        #statistics.mean([1,4,6,9])
#2,計算中位數--median
    #import statistics
        #statistics.median([1,4,6,9])
#3,計算標準差--stdev (代表資料散佈的狀況,差距會不會很大)standard deviation
    #import statistisc
        #statistisc.stdev([1,4,6,9])
#---------------------------------------------------------------------------#練習開始
#隨機模式

# import random
# data=random.choice([1,3,4,5,6,7])
# print('Choice:',data)

# data=random.sample([2,4,6,8,10,18],3)
# print('Sample:',data)

# data=([5,6,7,8,9,10])
# random.shuffle(data)
# print('Shuffle:',data)

# data=random.random()
# print('Random:',data)

# data=random.uniform(10,100)
# print('Uniform:',data)

# data=random.normalvariate(200,10)
# print('NormalVariate:',data)


#統計模式
import statistics as stat
data=stat.mean([1,2,3,4,5,6])
print('Average:',data)

data=stat.median([10,20,30,40,200,400])
print('Median:',data)

data=stat.stdev ([1,2,3,4,5,8])
print('Standard Devesion:',data)