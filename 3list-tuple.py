# # #有序可變動列表 LIST [一定用中刮號]
# grades =[12,60,15,70,90]
# grades [0] =55  #把55 放到列表中的第一位置
# print (grades )

# #有序可變動列表 LIST
grades =[12,60,15,70,90]
grades[1:4] =[]  #將位置1-4(60,15,70)的刪除即空格,只餘下12 和90
print (grades )

# #有序可變動列表 LIST
# grades =[12,60,15,70,90]
# grades =grades+[99,100]   #也可直接加入新的字串
# print (grades )

# #有序可變動列表 LIST
# grades =[12,60,15,70,90]
# length = len(grades) #len 取得列表長度len (列表資料)
# print (length )

# Weekdays= [1,2,3,4,5,6,7]
# val= len(Weekdays)
# print(val)

#有序可變動列表 LIST 巢狀列表例字

# data=[[3,4,5],[6,7,8]]
# data[0][0:2]=[5,5,5] #這是data 可選位置來取替,[0]是第一組數[0:2]從第一個位置數下去,即全部替換成5,5,5
# print (data)

# data=[[3,4,5],[6,7,8]]
# data[1][0:2]=[5,5,5] #這是data 可選位置來取替,[0]是第一組數[0:2]從第一個位置數下去,即全部替換成5,5,5
# print (data)



#有序不可動列表 Tuple 一定用刮號

# data=(3,4,5)
# data[0]=5  #錯誤,因為TUPLE是不能更改任何變量,所以會有錯誤訊息
# print (data)

