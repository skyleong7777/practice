# with open ('datatest.txt',mode='w',encoding='utf-8') as file:
#     file.write('3\n4\n5')

# sum=0
# with open('datatest.txt',mode='r') as file:

#     for i in (file):
#         sum+=int(i)    
#     print(sum)

# import json
# with open('config1.json',mode='r') as file:
#     print(json.load(file))
# import json
# with open('config.json',mode='r') as file:
#      data =json.load(file)
#      data['name']='this is a new'
# import json
# with open('config.json',mode='w') as file:
#     json.dump(data,file)
# with open('config.json',mode='r') as file:
#     print(json.load(file))

# import json
# with open ('config.json',mode='r') as file:
#     show=json.load(file)
#     show['gender']=[]
#     show['another']='test'
# with open('config.json',mode='w') as file:
#     json.dump(show,file)
# with open('config.json',mode='r') as file:
#     print(json.load(file))  

with open ('datatest.txt',mode='w') as file:
    file.write('6\n7\n8\n9')
sum=0
with open('datatest.txt',mode='r') as file:
    for number in file:
        sum+=(int(number))
print(sum)