
import re

path =re.sub(r'\\','/','D:\\other-project\wordDemo\python入门\day1\\text.txt')
print(path)

#w+ 读写模式，文件不存在会创建文件，r+ 文件不存在会抛出异常， a 追加模式，在末尾添加
# file = open(path,'w+')
# file = open('text.txt','a+',encoding='utf-8',errors='ignore')
# file.write('\nheellll')

# 案例抛出异常
# file = None
# try:
#     file = open(path,'r+',encoding='utf-8',errors='ignore')
#     print(file.read())
# except:
#     print('文件不存在')
# finally:
#     if file != None:
#        file.close()
#        print('文件关闭')

with(open(path,'r+') as f):
   lines= f.readlines()
   with(open('text1.txt','r+') as f1):
      f1.writelines(lines)
    