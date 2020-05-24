# 定義函數
#函式內部的程式碼,若沒有做函式呼喚,就不會執行,函式語法def 函式名稱(變數名稱):
def multiple (n1,n2):
     print(n1*n2)
     return n1*n2
# #呼叫函式
value=multiple(3,4)+multiple(10,5) #(3*4)+(10*5)
print (value)
#multiple(3,4)
#multiple(10,8)

#Def 程式的包裝,也是重要的的功能.而且同樣的邏輯可以重複使用
# sum=0
# for n in range(1,11):
#     sum=sum+n
#     #print(sum+n)       print 是在程式裏運行便會列出每一個數值
# print(sum)              #prnt 在外面即只有一個結果列印出來
#如何將以上的計算重複使用運算
# def calculate (x):        #可透過變量來更靈活處理Def ,把變量放入值
#     sum=0
#     for n in range(1,x+1):
#         sum=sum+n
#     print(sum)
# calculate(10)               #再透過呼叫來處理運算
# calculate(20)
# calculate(30)

