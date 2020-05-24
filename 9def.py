# 基本語法
#def 函式名稱(參數名稱=預設資料):形式一
    #函式內部的程式碼
# def say(msg='hello'): # example 1
#     print(msg)
# say('hello function')
# say()
# def power (base,exp=0): # example 2
#     i= base**exp
#     print(i)
# power (3,2)
# power (4)

#def 函式名稱(名稱1,名稱2):形式二
    #函式內部的程式碼
#呼叫函式,以參數名稱對應資料
    #函式名稱(名稱2=3,名稱1=5) 可不管順序
# def divide (n1,n2): #example 2
#     result=n1/n2
#     print(result)
# divide (2,4)    #印出0.5
# divide(n2=2,n1=4) #印出2

#無限/不定參數 - 形式三
# def 函式名稱 (*無限參數): 一定要在無限參數前面放*, 以無限參數是以Tuple資料型態處理
#       函式內部的程式碼
#呼叫函式,可傳入無限數的參數
#函式名稱(資料一,資料二,資料三)

# def say(*msg): # example3
#     for msg in msg:
#         print(msg)
# say('apple','ant','any')

def avg (*ns): #這是一個算平均數的例子,首先運用函式,由於很多數值便可以用*變數來處理
    sum=0
    for i in ns:
        sum=sum+i
    print(sum/len(ns))
avg(3,4,5)
avg(-2,-2,-2,-2)
avg(10,10,20)


