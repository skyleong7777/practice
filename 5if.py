# #if XXX :  第一個條件的IF 中間空, 記得加冒號:
#     #XXX    記得用TAB 做縮排,因為是關連部分,若布林值為TRUE 則行使命令
# #elif XXX: 若多於一個條件的IF,便要用ELIF 中間空, 記得加冒號:
#     #XXX     記得用TAB 做縮排,因為是關連部分,若布林值為TRUE 則行使命令
# #else XXX : 其它則是ELSE, 若布林值一和二都FLASE, 則行使命令

# # x=input('please enter any number: ') #取字串形式
# # x=int(x) # 將字串轉換成整數
# # if x>200:
# #     print ('this number is bigger or equal 200')
# # elif x>100:
# #     print ('this number is bigger or equal 100')
# # else:
# #     print ('this number is under 100 & 200')

# # #Switch 這語法暫時PYTHON 是不支持

# # x1= int(input('請輸入第一數值作運算='))
# # x2= int(input('請輸入第二個數值作運算='))
# # op= input ('+,-,*,/,=')

# # if op =='+':
# #     print(x1+x2)
# # elif op=='-':
# #     print(x1-x2)
# # elif op=='*':
# #     print(x1*x2)
# # elif op=='/':
# #     print(x1/x2)
# # else:
# #     print('不支援運計')
 

x1=float(input('please enter the first number: '))
x2=float(input('please enter the second number: '))
x3=float(input('please enter the third number: '))
x4=float(input('please enter the fourth number: '))
outcome= input('which calculation to you like to selec it +,-,*,/: ')

if outcome =='+':
     print(x1+x2+x3+x4)
elif outcome=='-':
     print(x1-x2-x3-x4)
elif outcome=='*':
     print(x1*x2*x3*x4)
elif outcome=='/':
     print(x1/x2/x3/x4)
else:
     print('Not support this calcuation')

