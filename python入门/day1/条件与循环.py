
# score = int(input('请输入一个正整数'))

# if(score >= 90):
#     print('优秀')
# elif(score >= 80):
#     print('良好')
# elif(score >= 70):
#     print('一般')
# elif(score >= 60):
#     print('及格')
# else:
#     print('不及格')

# if(score > 60):
#     print('及格')
# else:
#     print('不及格')

# i = 1

# while(i < 10):
   
#     i+=1
#     if(i==5):
#         break
#     print(i)
# else:
#     print('结束')

# obj={'name':'张三','age':18,'gender':'男'}

# obj=['name','age','gender']

# obj=5

# for item in range(obj):
#     print(item)

# for item in obj:
#     print(item)

i = 100;r =0; s =0; t=0

while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    # print(s,r)
    # break
    t = i - r * 100 - s * 10
    if i == (r ** 3 + s ** 3 + t ** 3):
        print('i = ' + str(i))
    i+=1
