# #break 的簡易範例
# n=0
# while n<5:
#     if n==3:
#         break            #如是if =ture 即3=3 時,程式便停止
#     print ('中間的:',n)
#     n+=1
# print('最後的',n)


# #continue 的簡易範例
# n=0   #N要在這個列表行走4次本來,但加了IF和CONTINUE 就不同了
# for x in [0,1,2,3]:
#     if x%2==0: #但加了if 和continue 後就會判斷做了多少次
#         continue     # 第一個執行0,由於0可比2整除,所以直接continue 以不會執行下邊print 和計算,但1和3 不同,因為不能continue 所以就會print 了數值出來,以最後只跑了兩次
#     print(x)
#     n+=1   #如沒有中間的IF,答案是4,因為在這循環跑了4次
# print('the last time is : ',n)  #n 只執行了兩次,所以得出2

#else 的簡易範例
sum=0
for i in range(11): 
    sum+=i
   
else:               #加了ELSE 後直接列出答案的總和55,沒了else 就每次SUM 後一個答案
    print(sum)

#綜合範例 練習1:開平方
# n=int(input('請輸入一數字當開平方根:'))
# for i in range(n):
#     if i*i==n:
#         print('this is an answer:',i)
#         break
# else:
#     print('不支援此數為平方根')