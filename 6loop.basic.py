# while 布林值(即TRUE or false):
#   若布林值為TRUE 則行使命令 (要縮排啊)跟IF 一樣
#   回到上方,做下一次的迴圈判斷 (不停運輚) (要縮排啊)

# while 迴圈
n=1
sum=0 #記錄累加的結果
while n<=10:
    #sum=sum+n
    sum+=n
    n+=1
print(sum)
# for 變數名稱 in 列表[]或字串'' (range):
    # 將列表中的填目或字串中的 (記得縮排)
    # 字元/數字逐一取出,逐一處理

#使用 range () 一般FOR 會和Range 一起使用
# for 變數名稱 in range (3): 記得加冒號, 這是只有開頭的例如3,就會如下顯示
# 相當於 (第一種用法) 
# for 變數名稱 in [0,1,2]:
# for 變數名稱 in range (3,6): 記得加冒號, 這是只有開頭的例如3,結尾寫6,只會顯示5 (即不包括6)
# 相當於 (第二種用法) 
# for 變數名稱 in [3,4,5]: 
sum=0
for x in range (11):
    sum=sum+x
print(sum)

