# 集合運算
# s1={3,4,5}
# print (10 not in s1)

#s1={3,4,5}
#s2={4,5,6,7}
#s3= s1&s2 # & 交集,兩個集合中,相同的資料 {4,5}
#s3= s1|s2 # | 聯集,取兩個集合中所有資料,但不重複 {3,4,5,6,7}
#s3=s1-s2   # 差集,從S1中減少S2重愎部分 {3}
#s3=s2-s1    {6,7}
#s3=s1^s2 # 只顯示沒重複的數值或部分 {3,6,7}
#print(s3)  

# s= set('Hello') #把字串的字母拆解成集合. 把重複文字/部分刪去)
# print(s)

# s= set('Hello') #把字串的字母拆解成集合. 判斷KEY是否存在
# print('H' in s)  #例如選H來測試在S 字串裏嗎? 答案是TRUE

#字典運算 #key=value 配對,例如SKY等於天空等,也可以中途變值
# dic={'Sky':'天空','Zero':'零'}
# dic['Sky']= '小天空'
# print (dic['Sky'])

# dic={'Sky':'天空','Zero':'零'}
# dic['Zero']='SKY+ZERO'
# print(dic['Zero'])

# dic={'Sky':'天空','Zero':'零'}
# print ('test' in dic)

# dic={'Sky':'天空','Zero':'零'}
# del dic['Zero']
# print(dic)

#dic ={x:x*2 for x in [3,4,5]} #for 咩咩咩 in range 一定要係列表 即中刮號[],亦因為係一個DICTIONORY 所以記得用: 來做KEY=VALUE
#print (dic)

# dic ={i:i+1 for i in [2,3,4,5,6]}

# print(dic)
# print(1 not in dic)